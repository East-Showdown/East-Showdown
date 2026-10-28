# -*- coding: utf-8 -*-
"""
East Showdown - build_cost_ic / supply_consumption calculator.

Reads the formulas from balance_settings.py (same folder) and recalculates
equipment in common/units/equipment and modules in common/units/equipment/modules.

Usage (from anywhere):
    python tools/balance/balance_calc.py                 # dry run: show what would change
    python tools/balance/balance_calc.py --write         # apply changes to the files
    python tools/balance/balance_calc.py --only ic       # only build_cost_ic (or: supply)
    python tools/balance/balance_calc.py --profile hull  # only items using that profile
    python tools/balance/balance_calc.py --name "*t72*"  # only matching names
    python tools/balance/balance_calc.py --explain sov_tank_main_gun_t55_D10T2S
    python tools/balance/balance_calc.py --unmapped      # list items no rule covers
    python tools/balance/balance_calc.py --csv report.csv

Nothing is written without --write. Formatting, comments, encoding and line
endings of the game files are preserved; only the numbers change.
"""
from __future__ import print_function

import argparse
import csv
import fnmatch
import glob
import importlib.util
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
EQUIP_DIR = os.path.join(REPO, "common", "units", "equipment")
MODULE_DIR = os.path.join(EQUIP_DIR, "modules")


# ---------------------------------------------------------------------------
# Paradox script parser that keeps text positions (so we can edit in place)
# ---------------------------------------------------------------------------
_TOKEN = re.compile(r'#[^\n]*|"[^"]*"|[{}]|[<>!]=|[=<>]|[^\s{}=<>!#"]+|!')
_OPS = ("=", "<", ">", "<=", ">=", "!=")


class Entry(object):
    __slots__ = ("key", "value", "start", "end")

    def __init__(self, key, value, start, end):
        self.key, self.value, self.start, self.end = key, value, start, end


class Block(object):
    """List of entries. value is str (scalar) or Block. open/close = positions of braces."""

    def __init__(self, open_pos, close_pos=None):
        self.entries = []
        self.open = open_pos
        self.close = close_pos

    def get(self, key, default=None):
        for e in self.entries:
            if e.key == key:
                return e
        return default

    def scalars(self):
        out = {}
        for e in self.entries:
            if e.key is not None and isinstance(e.value, str):
                out[e.key] = e.value
        return out

    def blocks(self):
        return [e for e in self.entries if isinstance(e.value, Block)]


def parse(text):
    toks = [(m.group(0), m.start(), m.end()) for m in _TOKEN.finditer(text)
            if not m.group(0).startswith("#")]
    pos = [0]

    def block(open_pos):
        b = Block(open_pos)
        while pos[0] < len(toks):
            t, s, e = toks[pos[0]]
            pos[0] += 1
            if t == "}":
                b.close = s
                return b
            if t == "{":
                b.entries.append(Entry(None, block(s), s, None))
                continue
            if pos[0] < len(toks) and toks[pos[0]][0] in _OPS:
                pos[0] += 1
                if pos[0] >= len(toks):
                    break
                vt, vs, ve = toks[pos[0]]
                pos[0] += 1
                if vt == "{":
                    b.entries.append(Entry(t, block(vs), s, None))
                else:
                    b.entries.append(Entry(t, vt, vs, ve))
            else:
                b.entries.append(Entry(None, t, s, e))
        b.close = len(text)
        return b

    return block(-1)


def num(v, default=0.0):
    try:
        return float(str(v).strip('"'))
    except (TypeError, ValueError):
        return default


# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------
def load_settings(path):
    spec = importlib.util.spec_from_file_location("balance_settings", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _match(patterns, value):
    if isinstance(patterns, str):
        patterns = [patterns]
    return value is not None and any(fnmatch.fnmatchcase(value, p) for p in patterns)


def find_rule(rules, **attrs):
    for r in rules:
        ok = True
        for k in ("file", "archetype", "type", "category", "name"):
            if k in r and not _match(r[k], attrs.get(k)):
                ok = False
                break
        if ok:
            return r
    return None


# ---------------------------------------------------------------------------
# Item model
# ---------------------------------------------------------------------------
class Item(object):
    def __init__(self, kind, name, path, text_ref, block, stats, mult, attrs, stat_block):
        self.kind = kind            # "equipment" | "module"
        self.name = name
        self.path = path
        self.text_ref = text_ref    # FileDoc
        self.block = block          # the item's block
        self.stats = stats          # effective stats (with inheritance)
        self.mult = mult            # multiply_stats (modules)
        self.attrs = attrs          # rule matching attributes
        self.stat_block = stat_block  # block holding build_cost_ic/supply (equipment block or add_stats)
        self.own = stat_block.scalars() if stat_block is not None else {}


class FileDoc(object):
    def __init__(self, path):
        self.path = path
        with open(path, "rb") as f:
            raw = f.read()
        self.bom = raw.startswith(b"\xef\xbb\xbf")
        self.text = raw.decode("utf-8-sig", errors="replace")
        self.newline = "\r\n" if "\r\n" in self.text else "\n"
        self.root = parse(self.text)
        self.edits = []  # (start, end, replacement)

    def save(self):
        if not self.edits:
            return
        text = self.text
        for s, e, rep in sorted(self.edits, key=lambda x: x[0], reverse=True):
            text = text[:s] + rep + text[e:]
        data = text.encode("utf-8")
        if self.bom:
            data = b"\xef\xbb\xbf" + data
        with open(self.path, "wb") as f:
            f.write(data)


def _indent_of_block(text, block):
    """Indentation used by the entries of a block (fallback: brace line + tab)."""
    for e in block.entries:
        if e.key is not None:
            ls = text.rfind("\n", 0, e.start) + 1
            # key starts before value; find the key position on this line
            line = text[ls:e.start]
            m = re.match(r"[ \t]*", line)
            return m.group(0)
    ls = text.rfind("\n", 0, block.open) + 1
    m = re.match(r"[ \t]*", text[ls:block.open])
    return (m.group(0) if m else "") + "\t"


def load_items(settings):
    docs, items = [], []

    # ---- equipment ----
    for path in sorted(glob.glob(os.path.join(EQUIP_DIR, "*.txt"))):
        doc = FileDoc(path)
        docs.append(doc)
        fname = os.path.basename(path)
        archetypes = {}
        for top in doc.root.blocks():
            if top.key != "equipments":
                continue
            for e in top.value.blocks():
                sc = e.value.scalars()
                if sc.get("is_archetype") == "yes":
                    archetypes[e.key] = e.value
            for e in top.value.blocks():
                b = e.value
                sc = b.scalars()
                is_arch = sc.get("is_archetype") == "yes"
                arch_name = e.key if is_arch else sc.get("archetype")
                arch = archetypes.get(arch_name)
                type_ = sc.get("type") or (arch.scalars().get("type") if arch is not None else None)
                if type_ is None:
                    tb = (b.get("type") or (arch.get("type") if arch is not None else None))
                    if tb is not None and isinstance(tb.value, Block):
                        type_ = " ".join(x.value for x in tb.value.entries if isinstance(x.value, str))
                stats = {}
                if settings.INHERIT_FROM_ARCHETYPE and arch is not None and not is_arch:
                    stats.update({k: num(v) for k, v in arch.scalars().items()})
                stats.update({k: num(v) for k, v in sc.items()})
                attrs = {"file": fname, "archetype": arch_name, "type": type_,
                         "name": e.key, "is_archetype": is_arch}
                it = Item("equipment", e.key, path, doc, b, stats, {}, attrs, b)
                it.inherited = ({k: num(v) for k, v in arch.scalars().items()}
                                if arch is not None and not is_arch else {})
                items.append(it)

    # ---- modules ----
    for path in sorted(glob.glob(os.path.join(MODULE_DIR, "*.txt"))):
        doc = FileDoc(path)
        docs.append(doc)
        fname = os.path.basename(path)
        for top in doc.root.blocks():
            if top.key != "equipment_modules":
                continue
            for e in top.value.blocks():
                if e.key in ("limit",):
                    continue
                b = e.value
                sc = b.scalars()
                add = b.get("add_stats")
                mul = b.get("multiply_stats")
                add_b = add.value if add is not None and isinstance(add.value, Block) else None
                stats = {k: num(v) for k, v in add_b.scalars().items()} if add_b else {}
                mult = ({k: num(v) for k, v in mul.value.scalars().items()}
                        if mul is not None and isinstance(mul.value, Block) else {})
                attrs = {"file": fname, "category": sc.get("category"), "name": e.key,
                         "is_archetype": False}
                it = Item("module", e.key, path, doc, b, stats, mult, attrs, add_b)
                it.inherited = {}
                items.append(it)
    return docs, items


# ---------------------------------------------------------------------------
# Calculation
# ---------------------------------------------------------------------------
def calc(profile, stats, mult, kind, no_negative=()):
    parts = []
    total = profile.get("base", 0) or 0
    if total:
        parts.append(("base", None, None, total))
    for s, w in profile.get("weights", {}).items():
        v = stats.get(s, 0.0)
        if v < 0 and s in no_negative:
            parts.append((s + " (negative, ignored)", v, w, 0.0))
            continue
        if v:
            parts.append((s, v, w, v * w))
            total += v * w
    if kind == "module":
        for s, w in profile.get("mult_weights", {}).items():
            v = mult.get(s, 0.0)
            if v < 0 and s in no_negative:
                parts.append(("x " + s + " (negative, ignored)", v, w, 0.0))
                continue
            if v:
                parts.append(("x " + s, v, w, v * w))
                total += v * w
    return total, parts


def fmt(v, digits):
    v = round(v + 0.0, digits)
    if digits <= 0:
        return str(int(round(v)))
    s = "%.*f" % (digits, v)
    return "0." + "0" * digits if s.startswith("-0.") and float(s) == 0 else s


FIELDS = {"ic": "build_cost_ic", "supply": "supply_consumption"}


def evaluate(settings, items, only=None):
    results, unmapped = [], []
    no_negative = set(getattr(settings, "IC_IGNORE_NEGATIVE", ()))
    for it in items:
        if it.attrs.get("is_archetype") and settings.SKIP_ARCHETYPES:
            continue
        if any(fnmatch.fnmatchcase(it.name, p) for p in settings.EXCLUDE):
            continue
        rules = settings.EQUIPMENT_RULES if it.kind == "equipment" else settings.MODULE_RULES
        rule = find_rule(rules, **it.attrs)
        if rule is None or (rule.get("ic") is None and rule.get("supply") is None):
            unmapped.append((it, rule))
            continue
        for fkey in ("ic", "supply"):
            if only and fkey != only:
                continue
            pname = rule.get(fkey)
            if not pname:
                continue
            profile = (settings.IC_PROFILES if fkey == "ic" else settings.SUPPLY_PROFILES)[pname]
            field = FIELDS[fkey]
            total, parts = calc(profile, it.stats, it.mult, it.kind,
                                no_negative if fkey == "ic" else ())
            mult_k = rule.get(fkey + "_multiplier", 1.0)
            if mult_k != 1.0:
                parts.append(("x multiplier", mult_k, None, total * mult_k - total))
                total *= mult_k
            has_stats = any(p[0] not in ("base", "x multiplier") and "ignored" not in p[0] for p in parts)
            own = it.own.get(field)
            current = num(own) if own is not None else it.inherited.get(field, 0.0)
            digits = profile.get("round", 2)
            new_s = fmt(total, digits)
            status = "ok"
            if settings.KEEP_IF_NO_STATS and not has_stats and not profile.get("base"):
                status = "no-stats"
            elif abs(float(new_s) - current) > 1e-9:
                status = "change"
            results.append({
                "item": it, "field": field, "profile": pname, "current": current,
                "current_raw": own, "new": float(new_s), "new_s": new_s, "parts": parts,
                "status": status,
            })
    return results, unmapped


# ---------------------------------------------------------------------------
# Writing
# ---------------------------------------------------------------------------
def apply(results):
    touched = set()
    for r in results:
        if r["status"] != "change":
            continue
        it, doc, field = r["item"], r["item"].text_ref, r["field"]
        nl = doc.newline
        target = it.stat_block
        if target is not None:
            e = target.get(field)
            if e is not None and isinstance(e.value, str):
                doc.edits.append((e.start, e.end, r["new_s"]))
            else:
                ind = _indent_of_block(doc.text, target)
                ins = _line_insert_pos(doc.text, target.close)
                doc.edits.append((ins, ins, "%s%s = %s%s" % (ind, field, r["new_s"], nl)))
        else:
            # module without add_stats -> create one
            ind = _indent_of_block(doc.text, it.block)
            ins = _line_insert_pos(doc.text, it.block.close)
            doc.edits.append((ins, ins, "%sadd_stats = {%s%s\t%s = %s%s%s}%s"
                              % (ind, nl, ind, field, r["new_s"], nl, ind, nl)))
        touched.add(doc)
    for doc in touched:
        doc.save()
    return touched


def _line_insert_pos(text, close_pos):
    """Insert before the line holding the closing brace (or right before it)."""
    ls = text.rfind("\n", 0, close_pos) + 1
    if text[ls:close_pos].strip() == "":
        return ls
    return close_pos


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main(argv=None):
    ap = argparse.ArgumentParser(description="Recalculate build_cost_ic and supply_consumption.")
    ap.add_argument("--settings", default=os.path.join(HERE, "balance_settings.py"))
    ap.add_argument("--write", action="store_true", help="apply changes to the game files")
    ap.add_argument("--only", choices=["ic", "supply"], help="only one field")
    ap.add_argument("--profile", action="append", help="only items using this profile (repeatable)")
    ap.add_argument("--name", action="append", help="only names matching wildcard (repeatable)")
    ap.add_argument("--file", action="append", help="only files matching wildcard (repeatable)")
    ap.add_argument("--all", action="store_true", help="also list unchanged items")
    ap.add_argument("--explain", metavar="NAME", help="show the formula breakdown for items matching NAME")
    ap.add_argument("--unmapped", action="store_true", help="list items no rule covers")
    ap.add_argument("--csv", metavar="PATH", help="write a full report as CSV")
    args = ap.parse_args(argv)

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    settings = load_settings(args.settings)
    docs, items = load_items(settings)

    def keep(it):
        if args.name and not any(fnmatch.fnmatchcase(it.name, p) for p in args.name):
            return False
        if args.file and not any(fnmatch.fnmatchcase(os.path.basename(it.path), p) for p in args.file):
            return False
        return True

    items = [i for i in items if keep(i)]
    results, unmapped = evaluate(settings, items, args.only)
    if args.profile:
        results = [r for r in results if r["profile"] in args.profile]

    if args.explain:
        for r in results:
            if not fnmatch.fnmatchcase(r["item"].name, args.explain):
                continue
            it = r["item"]
            print("%s  [%s]  %s  profile=%s" % (it.name, os.path.basename(it.path), r["field"], r["profile"]))
            for name, v, w, c in r["parts"]:
                if v is None:
                    print("    %-22s %28s  %+.4f" % (name, "", c))
                elif w is None:
                    print("    %-22s %10g %17s  %+.4f" % (name, v, "", c))
                else:
                    print("    %-22s %10g x %-12g = %+.4f" % (name, v, w, c))
            print("    %-22s %28s  %s   (current %s)%s" % ("TOTAL", "", r["new_s"], _g(r["current"]),
                  "" if r["status"] != "no-stats" else "  - no relevant stats, kept"))
            print()
        return 0

    if args.unmapped:
        print("Items without a rule (or rule with ic=None and supply=None):")
        for it, rule in unmapped:
            print("  %-40s %-45s %s" % (os.path.basename(it.path), it.name,
                  it.attrs.get("archetype") or it.attrs.get("category")))
        print("%d items" % len(unmapped))
        return 0

    changes = [r for r in results if r["status"] == "change"]
    shown = results if args.all else changes
    cur_file = None
    for r in sorted(shown, key=lambda r: (r["item"].path, r["item"].block.open, r["field"])):
        p = os.path.relpath(r["item"].path, REPO)
        if p != cur_file:
            cur_file = p
            print("\n== %s" % p)
        diff = r["new"] - r["current"]
        mark = {"change": "*", "ok": " ", "no-stats": "-"}[r["status"]]
        print(" %s %-48s %-19s %10s -> %-10s (%+g) [%s]" % (
            mark, r["item"].name, r["field"], _g(r["current"]), r["new_s"], round(diff, 4), r["profile"]))

    n_ok = sum(1 for r in results if r["status"] == "ok")
    n_ns = sum(1 for r in results if r["status"] == "no-stats")
    print("\nChecked %d values: %d to change, %d already correct, %d kept (no relevant stats). "
          "%d items not covered by any rule (--unmapped)." % (len(results), len(changes), n_ok, n_ns, len(unmapped)))

    if args.csv:
        with io.open(args.csv, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f)
            w.writerow(["file", "item", "kind", "field", "profile", "current", "calculated", "diff", "status"])
            for r in results:
                it = r["item"]
                w.writerow([os.path.relpath(it.path, REPO), it.name, it.kind, r["field"], r["profile"],
                            _g(r["current"]), r["new_s"], round(r["new"] - r["current"], 4), r["status"]])
        print("Report written to %s" % args.csv)

    if args.write:
        touched = apply(results)
        print("Wrote %d changes into %d files." % (len(changes), len(touched)))
    elif changes:
        print("Dry run - nothing written. Add --write to apply.")
    return 0


def _g(v):
    return ("%.4f" % v).rstrip("0").rstrip(".") if v is not None else "-"


if __name__ == "__main__":
    sys.exit(main())
