"""Bulletin 09 — Object-Oriented Python"""

import boletines
from utils.menu import run_menu, make_exit
from boletines.boletin_09 import Book, FuelConsumption, Car, BankAccount


# ---------------------------------------------------------------------------
# 01. Book class
# ---------------------------------------------------------------------------
def exercise_01():
    """
    Create class Book with attributes: title, author, year, pages, rating.
    Implement: __init__, getters, setters, properties, display method.
    """
    print("\n--- Exercise 01: Book class ---")

    title  = input("Title  : ")
    author = input("Author : ")

    while True:
        try:
            year   = int(input("Year   : "))
            pages  = int(input("Pages  : "))
            rating = float(input("Rating (0–10): "))
            book   = Book(title, author, year, pages, rating)
            break
        except ValueError as e:
            print(f"  ERROR: {e}")

    book.display()

    print("\n  -- Updating rating via setter --")
    try:
        book.rating = float(input("  New rating: "))
        print(f"  Updated: {book}")
    except ValueError as e:
        print(f"  ERROR: {e}")


# ---------------------------------------------------------------------------
# 02. FuelConsumption class
# ---------------------------------------------------------------------------
def exercise_02():
    """
    Class FuelConsumption (car electronic dashboard):
    Attributes: km, litros, vMed, pGas.
    Methods: getTempo, consumoMedio, consumoEuros, setters.
    """
    print("\n--- Exercise 02: Fuel Consumption class ---")

    while True:
        try:
            km         = float(input("Distance driven (km)     : "))
            litres     = float(input("Fuel consumed (litres)   : "))
            avg_speed  = float(input("Average speed (km/h)     : "))
            fuel_price = float(input("Fuel price per litre (€) : "))
            dashboard  = FuelConsumption(km, litres, avg_speed, fuel_price)
            break
        except ValueError as e:
            print(f"  ERROR: {e}")

    dashboard.display()


# ---------------------------------------------------------------------------
# 03. Car and BankAccount classes
# ---------------------------------------------------------------------------
def exercise_03():
    """
    Class Car: get_speed, accelerate(value), brake(amount).
    Class BankAccount: deposit, withdrawal, transfer between accounts.
    """
    print("\n--- Exercise 03: Car and BankAccount classes ---")

    print("\n  -- Car --")
    car = Car()
    car.accelerate(50)
    car.accelerate(30)
    car.brake(20)
    car.brake(100)
    print(f"  Final: {car}")

    print("\n  -- BankAccount --")
    try:
        acc1 = BankAccount("Alice", 1000.00)
        acc2 = BankAccount("Bob",    500.00)
        print(f"  Created: {acc1}")
        print(f"  Created: {acc2}")
        acc1.deposit(250.00)
        acc2.withdraw(100.00)
        acc1.transfer(acc2, 300.00)
        print(f"\n  Final: {acc1}")
        print(f"  Final: {acc2}")
        print("\n  -- Testing overdraft protection --")
        acc2.withdraw(10000.00)
    except ValueError as e:
        print(f"  ERROR caught: {e}")


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

MENU_OPTIONS = {
    "1": ("Book class",                    exercise_01),
    "2": ("Fuel Consumption class",        exercise_02),
    "3": ("Car and BankAccount classes",   exercise_03),
    "0": ("Exit", make_exit("Bulletin 09 — Object-Oriented Python")),
}


def bulletin_menu_09():
    run_menu("Bulletin 09 — Object-Oriented Python", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_09()

# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("9", "Bulletin 09 — Object-Oriented Python", bulletin_menu_09)
