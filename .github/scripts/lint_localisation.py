#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Проверка файлов локализации HOI4!!!! (хойка молча пропускает файлы локализации которые не в UTF-8 с BOM или у которых заголовок не совпадает с папкой)

import os
import re
import sys

BOM = "﻿"
LOC_ROOT = "localisation"
ENTRY_RE = re.compile(r'^\s*([A-Za-z0-9_.\-]+):(\d*)\s*"(.*)"\s*(#.*)?$')
HEADER_RE = re.compile(r'^\s*l_([a-z]+):\s*$')


def lang_from_path(path):
    parts = path.replace("\\", "/").split("/")
    if LOC_ROOT in parts:
        idx = parts.index(LOC_ROOT)
        if idx + 1 < len(parts):
            return parts[idx + 1]
    return None


def dangling_color_escape(value):
    return value.endswith("§")


def check_file(path):
    problems = []
    folder_lang = lang_from_path(path)

    try:
        with open(path, "rb") as fh:
            rawbytes = fh.read()
    except OSError as exc:
        return [(0, f"не удалось прочитать файл: {exc}")]

    if not rawbytes.startswith(BOM.encode("utf-8")):
        problems.append((1, "нет UTF-8 BOM (HOI4 пропустит этот файл)", "error"))

    try:
        text = rawbytes.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        problems.append((0, f"невалидный UTF-8: {exc}", "error"))
        return problems

    seen_keys = {}
    header_lang = None
    for lineno, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        hm = HEADER_RE.match(line)
        if hm:
            header_lang = hm.group(1)
            if folder_lang and header_lang != folder_lang:
                problems.append((lineno, f"заголовок 'l_{header_lang}:' не совпадает с папкой '{folder_lang}'", "error"))
            continue

        m = ENTRY_RE.match(line)
        if not m:
            problems.append((lineno, f"кривая запись (ожидалось  KEY:0 \"значение\"): {stripped[:60]}", "error"))
            continue

        key, _version, value = m.group(1), m.group(2), m.group(3)
        if key in seen_keys:
            problems.append((lineno, f"повтор ключа '{key}' (впервые в строке {seen_keys[key]})", "warning"))
        else:
            seen_keys[key] = lineno

        if dangling_color_escape(value):
            problems.append((lineno, f"висячий '§' в конце '{key}'", "error"))

    if header_lang is None:
        problems.append((1, "нет строки-заголовка 'l_<язык>:'", "error"))

    return problems


def collect_files(args):
    if args:
        return [a for a in args if a.endswith(".yml") and LOC_ROOT in a.replace("\\", "/")]
    files = []
    for root, _, names in os.walk(LOC_ROOT):
        for name in names:
            if name.endswith(".yml"):
                files.append(os.path.join(root, name))
    return sorted(files)


def main(argv):
    files = collect_files(argv[1:])
    errors = 0
    warnings = 0
    bad = set()
    for path in files:
        for lineno, msg, severity in check_file(path):
            print(f"::{severity} file={path},line={lineno or 1}::{path}:{lineno}: {msg}")
            bad.add(path)
            if severity == "error":
                errors += 1
            else:
                warnings += 1

    print(f"\nПроверено файлов локализации: {len(files)}.")
    print(f"Ошибок: {errors}, предупреждений: {warnings} в {len(bad)} файле(ах).")
    if errors:
        print("Проверка локализации не пройдена.")
        return 1
    if warnings:
        print("Локализация валидна, но предупреждения выше стоит починить.")
    else:
        print("Файлы локализации в порядке.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
