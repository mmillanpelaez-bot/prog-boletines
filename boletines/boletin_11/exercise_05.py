"""Exercise 05 — CSV inventory manager"""

import csv
import os

INVENTORY_FILE  = "products.csv"
LOW_STOCK_FILE  = "low_stock.csv"
LOW_STOCK_LIMIT = 5
FIELDNAMES      = ["id", "name", "price", "stock"]


def _load_inventory() -> list[dict]:
    if not os.path.exists(INVENTORY_FILE):
        return []
    with open(INVENTORY_FILE, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def inventory_manager():
    print("\n--- Exercise 05: CSV inventory manager ---")

    products = _load_inventory()
    if not products:
        print(f"  ERROR: '{INVENTORY_FILE}' not found or empty.")
        print(f"  Expected columns: {FIELDNAMES}")
        return

    print(f"  Loaded {len(products)} product(s) from '{INVENTORY_FILE}'.\n")

    print(f"  {'ID':<6} {'Name':<25} {'Price':>8} {'Stock':>6} {'Value':>10}")
    print("  " + "-" * 60)

    total_value = 0.0
    for p in products:
        price = float(p["price"])
        stock = int(p["stock"])
        value = price * stock
        total_value += value
        print(f"  {p['id']:<6} {p['name']:<25} {price:>8.2f}€ {stock:>6}  {value:>9.2f}€")

    print("  " + "-" * 60)
    print(f"  {'Total inventory value:':>48} {total_value:>9.2f}€")

    low_stock = [p for p in products if int(p["stock"]) < LOW_STOCK_LIMIT]
    if low_stock:
        with open(LOW_STOCK_FILE, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(low_stock)
        print(f"\n  {len(low_stock)} product(s) with stock < {LOW_STOCK_LIMIT} "
              f"exported to '{LOW_STOCK_FILE}'.")
    else:
        print(f"\n  All products have stock >= {LOW_STOCK_LIMIT}. No low-stock export needed.")
