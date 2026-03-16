"""Exercise 02 — Word frequency counter"""

import os
import string

SUMMARY_FILE = "word_summary.txt"


def _clean_word(word: str) -> str:
    return word.strip(string.punctuation).lower()


def word_counter():
    print("\n--- Exercise 02: Word frequency counter ---")

    filename = input("  Enter filename (e.g. text.txt): ").strip()
    if not os.path.exists(filename):
        print(f"  ERROR: File '{filename}' not found.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()

    words     = [_clean_word(w) for w in raw.split() if _clean_word(w)]
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    sorted_freq = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

    print(f"\n  Total words : {len(words)}")
    print(f"  Unique words: {len(frequency)}")
    print(f"\n  {'Word':<20} Count")
    print("  " + "-" * 28)
    for word, count in sorted_freq[:20]:
        print(f"  {word:<20} {count}")

    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        f.write(f"Total words : {len(words)}\n")
        f.write(f"Unique words: {len(frequency)}\n\n")
        f.write(f"{'Word':<20} Count\n")
        f.write("-" * 28 + "\n")
        for word, count in sorted_freq:
            f.write(f"{word:<20} {count}\n")

    print(f"\n  Full summary saved to '{SUMMARY_FILE}'.")
