"""Exercise 01 — Personal note manager"""

import os

NOTES_FILE = "notes.txt"


def _load_notes() -> list[str]:
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if line.strip()]


def _save_notes(notes: list[str]) -> None:
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")
    print(f"  Notes saved to '{NOTES_FILE}'.")


def notes_manager():
    print("\n--- Exercise 01: Personal note manager ---")
    notes = _load_notes()
    print(f"  Loaded {len(notes)} existing note(s) from '{NOTES_FILE}'.")

    while True:
        print("\n  1. Add note")
        print("  2. List all notes")
        print("  3. Search notes")
        print("  4. Save and exit")
        choice = input("  >> ").strip()

        if choice == "1":
            text = input("  Note: ").strip()
            if text:
                notes.append(text)
                print(f"  Note added ({len(notes)} total).")
            else:
                print("  Empty note discarded.")

        elif choice == "2":
            if not notes:
                print("  No notes yet.")
            else:
                print(f"\n  --- {len(notes)} note(s) ---")
                for i, note in enumerate(notes, 1):
                    print(f"  {i:>3}. {note}")

        elif choice == "3":
            keyword = input("  Search keyword: ").strip().lower()
            matches = [(i + 1, n) for i, n in enumerate(notes) if keyword in n.lower()]
            if matches:
                print(f"\n  Found {len(matches)} match(es):")
                for idx, note in matches:
                    print(f"  {idx:>3}. {note}")
            else:
                print("  No matches found.")

        elif choice == "4":
            _save_notes(notes)
            break
        else:
            print("  Invalid option.")
