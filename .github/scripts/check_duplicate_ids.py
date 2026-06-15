#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# Поиск дублей id фокусов и событий в скрипте мода HOI4.

import os
import re
import sys

FOCUS_OPEN_RE = re.compile(r'\b(?:shared_focus|focus)\s*=\s*\{')
ID_RE = re.compile(r'^\s*id\s*=\s*([A-Za-z0-9_.\-]+)')
EVENT_ID_RE = re.compile(r'^\s*id\s*=\s*([A-Za-z0-9_]+\.\d+)')
EVENT_DEF_OPEN_RE = re.compile(r'^[A-Za-z_]*event\s*=\s*\{')


def strip_comment(line):
    out = []
    in_string = False
    for ch in line:
        if ch == '"':
            in_string = not in_string
        elif ch == "#" and not in_string:
            break
        out.append(ch)
    return "".join(out)


def collect_focus_ids(files):
    ids = {}
    for path in files:
        expecting = False
        try:
            lines = open(path, encoding="utf-8-sig", errors="replace").read().splitlines()
        except OSError:
            continue
        for lineno, raw in enumerate(lines, 1):
            line = strip_comment(raw)
            if FOCUS_OPEN_RE.search(line):
                expecting = True
            if expecting:
                m = ID_RE.match(line)
                if m:
                    ids.setdefault(m.group(1), []).append(f"{path}:{lineno}")
                    expecting = False
    return ids


def collect_event_ids(files):
    ids = {}
    for path in files:
        expecting = False
        try:
            lines = open(path, encoding="utf-8-sig", errors="replace").read().splitlines()
        except OSError:
            continue
        for lineno, raw in enumerate(lines, 1):
            line = strip_comment(raw)
            if EVENT_DEF_OPEN_RE.match(line):
                expecting = True
            if expecting:
                m = EVENT_ID_RE.match(line)
                if m:
                    ids.setdefault(m.group(1), []).append(f"{path}:{lineno}")
                    expecting = False
    return ids


def walk(root, suffix=".txt"):
    found = []
    for r, _, names in os.walk(root):
        for n in names:
            if n.endswith(suffix):
                found.append(os.path.join(r, n))
    return sorted(found)


def report(kind, ids, changed):
    collisions = {k: v for k, v in ids.items() if len(v) > 1}
    errors = 0
    warnings = 0
    for ident, locs in sorted(collisions.items()):
        files = {loc.rsplit(":", 1)[0] for loc in locs}
        is_error = (not changed) or bool(files & changed)
        severity = "error" if is_error else "warning"
        first = locs[0]
        for dup in locs[1:]:
            path, line = dup.rsplit(":", 1)
            print(f"::{severity} file={path},line={line}::дубль {kind} id "
                  f"'{ident}' (уже определён в {first})")
        if is_error:
            errors += 1
        else:
            warnings += 1
    print(f"{kind}: дублей id - {len(collisions)} "
          f"({errors} ошибок, {warnings} старых предупреждений) из {len(ids)} всего.")
    return errors


def main(argv):
    changed = {a.replace("\\", "/") for a in argv[1:]}
    focus_dirs = "common/national_focus"
    event_dirs = "events"

    n = 0
    if os.path.isdir(focus_dirs):
        n += report("focus", collect_focus_ids(walk(focus_dirs)), changed)
    if os.path.isdir(event_dirs):
        n += report("event", collect_event_ids(walk(event_dirs)), changed)

    if n:
        print(f"\nГрупп дублей id, затрагивающих изменённые файлы: {n}.")
        return 1
    print("\nНовых дублей id не добавлено.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
