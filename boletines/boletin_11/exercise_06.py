"""Exercise 06 — JSON contact book"""

import json
import os

CONTACTS_FILE = "contacts.json"


def _load_contacts() -> dict:
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_contacts(contacts: dict) -> None:
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)
    print(f"  Contacts saved to '{CONTACTS_FILE}'.")


def contact_book():
    print("\n--- Exercise 06: JSON contact book ---")
    contacts = _load_contacts()
    print(f"  Loaded {len(contacts)} contact(s).")

    while True:
        print("\n  1. Add contact")
        print("  2. List contacts")
        print("  3. Search contact")
        print("  4. Delete contact")
        print("  5. Save and exit")
        choice = input("  >> ").strip()

        if choice == "1":
            name = input("  Name  : ").strip()
            if not name:
                print("  Name cannot be empty.")
                continue
            if name in contacts:
                print(f"  '{name}' already exists.")
                continue
            email  = input("  Email : ").strip()
            phones = []
            while True:
                phone = input("  Phone (Enter to stop): ").strip()
                if not phone:
                    break
                phones.append(phone)
            contacts[name] = {"email": email, "phones": phones}
            print(f"  Contact '{name}' added.")

        elif choice == "2":
            if not contacts:
                print("  No contacts.")
            else:
                print(f"\n  --- {len(contacts)} contact(s) ---")
                for name, info in sorted(contacts.items()):
                    phones = ", ".join(info["phones"]) or "—"
                    print(f"  {name:<25} {info['email']:<30} {phones}")

        elif choice == "3":
            keyword = input("  Search name: ").strip().lower()
            matches = {n: i for n, i in contacts.items() if keyword in n.lower()}
            if not matches:
                print("  No matches.")
            else:
                for name, info in matches.items():
                    print(f"\n  Name  : {name}")
                    print(f"  Email : {info['email']}")
                    print(f"  Phones: {', '.join(info['phones']) or '—'}")

        elif choice == "4":
            name = input("  Contact name to delete: ").strip()
            if name in contacts:
                del contacts[name]
                print(f"  '{name}' deleted.")
            else:
                print("  Contact not found.")

        elif choice == "5":
            _save_contacts(contacts)
            break
        else:
            print("  Invalid option.")
