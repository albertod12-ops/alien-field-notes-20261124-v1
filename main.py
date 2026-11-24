"""Satu baris untuk kompetisi make.fun "Alien Field Notes" (v1).

Ulasan turis alien atas Bumi: manusia membayar untuk duduk di kotak logam
dan diguncang dengan keras, lalu menyebutnya menyenangkan. Matahari
terbenamnya indah, jadi ia mau kembali -- dengan sabuk pengaman.
Satu lelucon saja, punch-nya jatuh di dua kata terakhir.
"""

import os

TEXT = "★★★★☆ Earth: the locals pay to sit in a metal box and be shaken violently, then call it fun. Lovely sunsets, though. Would visit again — with a seatbelt."
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.umask(0o022)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
