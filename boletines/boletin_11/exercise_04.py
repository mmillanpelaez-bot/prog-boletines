"""Exercise 04 — Customer manager with binary file persistence"""

import os
import pickle

CUSTOMERS_FILE = "customers.dat"


class Customer:
    _next_id = 1

    def __init__(self, name: str, phone: str):
        self.id    = Customer._next_id
        Customer._next_id += 1
        self.name  = name
        self.phone = phone

    def display(self) -> None:
        print(f"  [{self.id:>3}] {self.name:<25} {self.phone}")

    def __str__(self) -> str:
        return f"Customer(id={self.id}, name='{self.name}', phone='{self.phone}')"


def _load_customers() -> list[Customer]:
    if not os.path.exists(CUSTOMERS_FILE):
        return []
    with open(CUSTOMERS_FILE, "rb") as f:
        customers = pickle.load(f)
    if customers:
        Customer._next_id = max(c.id for c in customers) + 1
    return customers


def _save_customers(customers: list[Customer]) -> None:
    with open(CUSTOMERS_FILE, "wb") as f:
        pickle.dump(customers, f)
    print(f"  Customers saved to '{CUSTOMERS_FILE}'.")


def customer_manager():
    print("\n--- Exercise 04: Customer manager ---")
    customers = _load_customers()
    print(f"  Loaded {len(customers)} customer(s).")

    while True:
        print("\n  1. Add customer")
        print("  2. List customers")
        print("  3. Update customer")
        print("  4. Remove customer")
        print("  5. Save and exit")
        choice = input("  >> ").strip()

        if choice == "1":
            name  = input("  Name  : ").strip()
            phone = input("  Phone : ").strip()
            customers.append(Customer(name, phone))
            print("  Customer added.")

        elif choice == "2":
            if not customers:
                print("  No customers.")
            else:
                print(f"\n  {'ID':>4}  {'Name':<25} Phone")
                print("  " + "-" * 42)
                for c in customers:
                    c.display()

        elif choice == "3":
            if not customers:
                print("  No customers.")
                continue
            try:
                cid    = int(input("  Customer ID to update: "))
                target = next((c for c in customers if c.id == cid), None)
                if not target:
                    print("  ID not found.")
                    continue
                name  = input(f"  New name  [{target.name}]  : ").strip()
                phone = input(f"  New phone [{target.phone}]: ").strip()
                if name:  target.name  = name
                if phone: target.phone = phone
                print("  Customer updated.")
            except ValueError:
                print("  Invalid ID.")

        elif choice == "4":
            if not customers:
                print("  No customers.")
                continue
            try:
                cid       = int(input("  Customer ID to remove: "))
                before    = len(customers)
                customers = [c for c in customers if c.id != cid]
                print("  Customer removed." if len(customers) < before else "  ID not found.")
            except ValueError:
                print("  Invalid ID.")

        elif choice == "5":
            _save_customers(customers)
            break
        else:
            print("  Invalid option.")
