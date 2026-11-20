"""Load HOI4 focus trees and resolve focus positions."""

import glob
import io
import itertools
import os
import re

import pdx

AUTO_ONLY_RE = re.compile(r"\b\w*_auto_focus_only_tt\b")


def read_text(path):
    with io.open(path, "r", encoding="utf-8-sig", errors="replace") as f:
        return f.read()


class Focus(object):
    def __init__(self, fid, path, text, node, shared):
        self.id = fid
        self.path = path
        self.text = text
        self.node = node
        self.shared = shared
        items = node.value
        self.x = float(pdx.val(items, "x", "0"))
        self.y = float(pdx.val(items, "y", "0"))
        self.rel = pdx.val(items, "relative_position_id")
        self.offsets = []
        for off in pdx.get_all(items, "offset"):
            if not off.is_block():
                continue
            trig = pdx.get(off.value, "trigger")
            self.offsets.append((
                float(pdx.val(off.value, "x", "0")),
                float(pdx.val(off.value, "y", "0")),
                pdx.raw_inner(text, trig).strip() if trig is not None and trig.is_block() else None,
            ))
        self.prereq_groups = []
        for pr in pdx.get_all(items, "prerequisite"):
            if pr.is_block():
                grp = [n.value for n in pr.value if n.key == "focus" and not n.is_block()]
                if grp:
                    self.prereq_groups.append(grp)
        self.mutex = []
        for me in pdx.get_all(items, "mutually_exclusive"):
            if me.is_block():
                self.mutex += [n.value for n in me.value if n.key == "focus" and not n.is_block()]
        av = pdx.get(items, "available")
        self.available_raw = pdx.raw_inner(text, av).strip() if av is not None and av.is_block() else ""
        self.available_node = av
        ab = pdx.get(items, "allow_branch")
        self.allow_branch_raw = pdx.raw_inner(text, ab).strip() if ab is not None and ab.is_block() else ""
        self.available_if_capitulated = pdx.val(items, "available_if_capitulated", "no") == "yes"
        self.icon = self._icon(items)

    def _icon(self, items):
        for n in pdx.get_all(items, "icon"):
            if not n.is_block():
                return n.value
        # dynamic icon: icon = { trigger = {...} value = GFX } ; prefer the one without trigger
        cands = []
        for n in pdx.get_all(items, "icon"):
            if n.is_block():
                v = pdx.val(n.value, "value")
                if v:
                    cands.append((pdx.get(n.value, "trigger") is not None, v))
        cands.sort()
        return cands[0][1] if cands else "GFX_goal_unknown"

    def exclusion_reason(self):
        """Return why this focus cannot be started by the player, or None."""
        if AUTO_ONLY_RE.search(self.available_raw):
            return "auto"
        av = self.available_node
        if av is not None and av.is_block():
            for n in av.value:
                if n.key == "always" and n.value == "no":
                    return "never_available"
        return None

    def has_conditional_never(self):
        return self.exclusion_reason() is None and re.search(r"\balways\s*=\s*no\b", self.available_raw) is not None


class Tree(object):
    def __init__(self, tid, path, focus_ids, default):
        self.id = tid
        self.path = path
        self.focus_ids = focus_ids
        self.default = default


class Model(object):
    def __init__(self, focus_dir):
        self.focuses = {}
        self.trees = []
        self.shared = {}
        self.warnings = []
        tree_shared_refs = []
        for path in sorted(glob.glob(os.path.join(focus_dir, "*.txt"))):
            text = read_text(path)
            try:
                nodes = pdx.parse(text)
            except pdx.ParseError as e:
                self.warnings.append("%s: parse error: %s" % (os.path.basename(path), e))
                continue
            for top in nodes:
                if top.key == "shared_focus" and top.is_block():
                    f = self._add_focus(top, path, text, True)
                    if f:
                        self.shared[f.id] = f
                elif top.key == "focus_tree" and top.is_block():
                    tid = pdx.val(top.value, "id")
                    ids = []
                    refs = []
                    for n in top.value:
                        if n.key == "focus" and n.is_block():
                            f = self._add_focus(n, path, text, False)
                            if f:
                                ids.append(f.id)
                        elif n.key == "shared_focus" and not n.is_block():
                            refs.append(n.value)
                    tree = Tree(tid, path, ids, pdx.val(top.value, "default", "no") == "yes")
                    self.trees.append(tree)
                    tree_shared_refs.append((tree, refs))
        # expand shared focuses: the referenced roots plus every shared focus depending on them
        for tree, refs in tree_shared_refs:
            included = set()
            stack = [r for r in refs if r in self.shared]
            for r in refs:
                if r not in self.shared:
                    self.warnings.append("%s: unknown shared focus %s" % (tree.id, r))
            while stack:
                cur = stack.pop()
                if cur in included:
                    continue
                included.add(cur)
                for sf in self.shared.values():
                    if sf.id not in included and any(cur in g for g in sf.prereq_groups):
                        stack.append(sf.id)
            tree.focus_ids += sorted(included)

    def _add_focus(self, node, path, text, shared):
        fid = pdx.val(node.value, "id")
        if not fid:
            self.warnings.append("%s: focus without id at char %d" % (os.path.basename(path), node.start))
            return None
        if fid in self.focuses:
            self.warnings.append("duplicate focus id %s (%s and %s)" % (fid, self.focuses[fid].path, path))
            return self.focuses[fid]
        f = Focus(fid, path, text, node, shared)
        self.focuses[fid] = f
        return f

    # ---- layout ---------------------------------------------------------
    def position(self, fid, _seen=None):
        """Return (x, y, offsets) where offsets is a list of (dx, dy, trigger_raw)
        that apply to this focus (own + inherited through relative_position_id)."""
        _seen = _seen or set()
        f = self.focuses[fid]
        if fid in _seen:
            self.warnings.append("relative_position_id cycle at %s" % fid)
            return f.x, f.y, []
        _seen.add(fid)
        x, y = f.x, f.y
        offs = list(f.offsets)
        if f.rel:
            if f.rel in self.focuses:
                px, py, poffs = self.position(f.rel, _seen)
                x += px
                y += py
                offs = poffs + offs
            else:
                self.warnings.append("%s: relative_position_id %s not found" % (fid, f.rel))
        return x, y, offs

    def position_variants(self, fid, max_variants=16):
        """Yield (x, y, active_triggers, inactive_triggers) for each combination
        of conditional offsets. Unconditional offsets are always applied."""
        x, y, offs = self.position(fid)
        always = [(dx, dy) for dx, dy, t in offs if not t]
        cond = [(dx, dy, t) for dx, dy, t in offs if t]
        for dx, dy in always:
            x += dx
            y += dy
        if len(cond) > 4:
            self.warnings.append("%s: %d conditional offsets, only first 4 used for button placement" % (fid, len(cond)))
            cond = cond[:4]
        out = []
        for mask in itertools.product((False, True), repeat=len(cond)):
            vx, vy, act, inact = x, y, [], []
            for on, (dx, dy, t) in zip(mask, cond):
                if on:
                    vx += dx
                    vy += dy
                    act.append(t)
                else:
                    inact.append(t)
            out.append((vx, vy, act, inact))
        return out[:max_variants]
