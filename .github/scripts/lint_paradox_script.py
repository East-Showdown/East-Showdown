#!/usr/bin/env python3


# Проверка баланса скобок в файлах Paradox скрипта!!!!!

import os
import sys

DEFAULT_DIRS = ["common", "events", "history"]


def strip_comments_and_strings(line):
    out = []
    in_string = False
    i = 0
    while i < len(line):
        ch = line[i]
        if in_string:
            if ch == '"':
                in_string = False
        else:
            if ch == '"':
                in_string = True
            elif ch == '#':
                break
            else:
                out.append(ch)
        i += 1
    return "".join(out), in_string


def check_file(path):
    problems = []
    depth = 0
    in_string = False
    try:
        with open(path, "r", encoding="utf-8-sig", errors="replace") as fh:
            for lineno, raw in enumerate(fh, 1):
                if in_string:
                    problems.append((lineno, "незакрытая кавычка с предыдущей строки"))
                    in_string = False
                cleaned, in_string = strip_comments_and_strings(raw)
                for ch in cleaned:
                    if ch == "{":
                        depth += 1
                    elif ch == "}":
                        depth -= 1
                        if depth < 0:
                            problems.append((lineno, "лишняя '}' (закрывающих скобок больше, чем открывающих)"))
                            depth = 0
    except OSError as exc:
        return [(0, f"не удалось прочитать файл: {exc}")]

    if depth > 0:
        problems.append((0, f"в конце файла осталось незакрытых '{{': {depth}"))
    return problems


def collect_files(args):
    if args:
        return [a for a in args if a.endswith(".txt")]
    files = []
    for d in DEFAULT_DIRS:
        for root, _, names in os.walk(d):
            for name in names:
                if name.endswith(".txt"):
                    files.append(os.path.join(root, name))
    return sorted(files)


def main(argv):
    files = collect_files(argv[1:])
    total_problems = 0
    bad_files = 0
    for path in files:
        problems = check_file(path)
        if problems:
            bad_files += 1
            for lineno, msg in problems:
                loc = f"{path}:{lineno}" if lineno else path
                print(f"::error file={path},line={lineno or 1}::{loc}: {msg}")
                total_problems += 1

    print(f"\nПроверено файлов скрипта: {len(files)}.")
    if total_problems:
        print(f"Найдено проблем: {total_problems} в {bad_files} файле(ах).")
        return 1
    print("Проблем с балансом скобок не найдено.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
