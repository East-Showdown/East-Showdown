#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
reencode_ogg_128.py

Рекурсивно ищет *.ogg в соседней папке 'music' и перекодирует аудио в 128 kbps,
если текущий битрейт выше 128 kbps.

Использование:
  python reencode_ogg_128.py
  python reencode_ogg_128.py --dry-run        # только показать, что будет сделано
  python reencode_ogg_128.py --verbose        # подробный вывод
"""

import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Optional, Tuple

THRESHOLD_BITRATE = 128_000  # 128 kbps в бит/с
EPSILON = 5000               # небольшой зазор на погрешности (≈5 kbps)

def run(cmd: list[str]) -> Tuple[int, str, str]:
    """Запуск команды и возврат (rc, stdout, stderr)."""
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = proc.communicate()
    return proc.returncode, out, err

def ffprobe_info(path: Path) -> dict:
    """Возвращает JSON c информацией ffprobe для файла."""
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "a:0",
        "-show_entries", "stream=bit_rate,codec_name",
        "-show_entries", "format=bit_rate,duration",
        "-of", "json", str(path)
    ]
    rc, out, err = run(cmd)
    if rc != 0:
        raise RuntimeError(f"ffprobe error ({rc}) on {path}: {err.strip()}")
    try:
        return json.loads(out)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Cannot parse ffprobe output for {path}: {e}")

def extract_bitrate_and_codec(info: dict, path: Path) -> Tuple[Optional[int], Optional[str]]:
    """Достаёт оценку битрейта (бит/с) и имя кодека из ffprobe JSON."""
    bitrates = []
    codec_name = None

    streams = info.get("streams") or []
    if streams:
        s0 = streams[0]
        codec_name = s0.get("codec_name")
        br = s0.get("bit_rate")
        if br:
            try:
                bitrates.append(int(br))
            except ValueError:
                pass

    fmt = info.get("format") or {}
    fmt_br = fmt.get("bit_rate")
    if fmt_br:
        try:
            bitrates.append(int(fmt_br))
        except ValueError:
            pass

    # Если точного битрейта нет — оцениваем по размеру и длительности
    if not bitrates:
        dur = fmt.get("duration")
        try:
            duration = float(dur) if dur is not None else None
        except ValueError:
            duration = None
        if duration and duration > 0:
            try:
                size_bytes = path.stat().st_size
                approx = int(size_bytes * 8 / duration)  # бит/с
                bitrates.append(approx)
            except OSError:
                pass

    bitrate = max(bitrates) if bitrates else None
    return bitrate, codec_name

def choose_encoder(codec_name: Optional[str]) -> Tuple[str, list[str]]:
    """
    Возвращает имя кодека и список параметров ffmpeg для перекодирования в 128 kbps.
    Сохраняем семейство кодека, если возможно.
    """
    if codec_name == "opus":
        return "libopus", ["-c:a", "libopus", "-b:a", "128k"]
    # По умолчанию — Vorbis в OGG
    return "libvorbis", ["-c:a", "libvorbis", "-b:a", "128k", "-compression_level", "5"]

def transcode_to_128(input_path: Path, dry_run: bool = False, verbose: bool = False) -> bool:
    """
    Перекодирует файл на месте через временный файл.
    Возвращает True, если перекодирование выполнено.
    """
    info = ffprobe_info(input_path)
    bitrate, codec_name = extract_bitrate_and_codec(info, input_path)

    if bitrate is None:
        if verbose:
            print(f"[?] {input_path} — текущий битрейт не удалось определить, пропуск.")
        return False

    if bitrate <= THRESHOLD_BITRATE + EPSILON:
        if verbose:
            print(f"[=] {input_path} — {bitrate/1000:.1f} kbps, <= 128 kbps. Пропуск.")
        return False

    enc_name, enc_args = choose_encoder(codec_name)
    if verbose:
        print(f"[>] {input_path} — {bitrate/1000:.1f} kbps → перекодирование в 128 kbps ({enc_name}).")

    if dry_run:
        return False

    tmp_out = input_path.with_name(input_path.stem + ".tmp.ogg")
    # Собираем команду ffmpeg
    cmd = [
        "ffmpeg", "-y",
        "-i", str(input_path),
        "-vn",
        "-map", "0:a:0?",
        *enc_args,
        "-map_metadata", "0",
        "-f", "ogg",                 # <— добавили
        str(tmp_out)
    ]

    rc, out, err = run(cmd)
    if rc != 0 or not tmp_out.exists():
        if tmp_out.exists():
            tmp_out.unlink(missing_ok=True)
        raise RuntimeError(f"ffmpeg error ({rc}) on {input_path}:\n{err.strip()}")

    # Атомарная замена исходника
    backup = input_path.with_suffix(input_path.suffix + ".bak")
    try:
        shutil.move(str(input_path), str(backup))
        shutil.move(str(tmp_out), str(input_path))
        backup.unlink(missing_ok=True)  # всё ок — удаляем бэкап
    except Exception:
        # В случае сбоя пытаемся откатить
        if tmp_out.exists():
            tmp_out.unlink(missing_ok=True)
        if backup.exists() and (not input_path.exists()):
            shutil.move(str(backup), str(input_path))
        raise
    return True

def main():
    parser = argparse.ArgumentParser(description="Рекодер .ogg > 128 kbps → 128 kbps в папке music")
    parser.add_argument("--dry-run", action="store_true", help="Только показать, что будет сделано")
    parser.add_argument("--verbose", action="store_true", help="Подробный вывод")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent.parent
    music_dir = script_dir.parent / "music"

    if not music_dir.exists() or not music_dir.is_dir():
        raise SystemExit(f"Папка 'music' не найдена рядом с 'tools'. Ожидалось: {music_dir}")

    total = 0
    changed = 0
    skipped = 0
    errors = 0

    for ogg in music_dir.rglob("*.ogg"):
        total += 1
        try:
            did = transcode_to_128(ogg, dry_run=args.dry_run, verbose=args.verbose)
            if did:
                changed += 1
            else:
                skipped += 1
        except Exception as e:
            errors += 1
            print(f"[!] Ошибка: {ogg}\n    {e}")

    print("\nИТОГО:")
    print(f"  Найдено .ogg: {total}")
    print(f"  Перекодировано: {changed}")
    print(f"  Пропущено: {skipped}")
    print(f"  Ошибок: {errors}")
    if args.dry_run:
        print("Режим: dry-run (ничего не менялось).")

if __name__ == "__main__":
    main()
