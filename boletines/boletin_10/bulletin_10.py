"""Bulletin 10 — Exceptions"""

import boletines
from utils.menu import run_menu, make_exit
from boletines.boletin_10 import Person, Athlete, Date, InvalidDniError, InvalidLicenceError, InvalidDateError


# ---------------------------------------------------------------------------
# 01. Persoa / Deportista with custom exceptions
# ---------------------------------------------------------------------------
def exercise_01():
    """
    Classes Persoa and Deportista.
    setter for DNI raises DniNonValido if format is incorrect.
    setLicenza validates format aaaadddnnnnnn:
      - aaaa: 4-digit year
      - ddd:  sport abbreviation (fut, bal, etc.)
      - nnnnnn: 6-digit unique licence number
    """
    print("\n--- Exercise 01: Person and Athlete classes ---")

    print("\n  -- Creating a Person --")
    while True:
        try:
            name = input("  Name : ")
            dni  = input("  DNI  : ").strip().upper()
            p    = Person(name, dni)
            p.display()
            break
        except InvalidDniError as e:
            print(f"  ERROR: {e}")

    print("\n  -- Creating an Athlete --")
    while True:
        try:
            name    = input("  Name    : ")
            dni     = input("  DNI     : ").strip().upper()
            licence = input("  Licence (e.g. 2024fut000123): ").strip().lower()
            a       = Athlete(name, dni, licence)
            a.display()
            break
        except (InvalidDniError, InvalidLicenceError) as e:
            print(f"  ERROR: {e}")


# ---------------------------------------------------------------------------
# 02. Data class with full validation
# ---------------------------------------------------------------------------
def exercise_02():
    """
    Class Data with validated day/month/year, raising FormatoDataError on bad input.
    Rules:
      - Day: 1 to 28/29/30/31 depending on month and leap year
      - Month: 1 to 12
      - Year: 1970 to 2999
    """
    print("\n--- Exercise 02: Date class with validation ---")

    while True:
        try:
            day   = int(input("  Day   (1–31)      : "))
            month = int(input("  Month (1–12)      : "))
            year  = int(input("  Year  (1970–2999) : "))
            date  = Date(day, month, year)
            date.display()
            break
        except (InvalidDateError, ValueError) as e:
            print(f"  ERROR: {e}")

    print("\n  -- Testing invalid date (Feb 30) --")
    try:
        d = Date(1, 1, 2024)
        d.month = 2
        d.day   = 30
    except InvalidDateError as e:
        print(f"  ERROR caught correctly: {e}")

    print("\n  -- Testing leap year (Feb 29, 2024) --")
    try:
        Date(29, 2, 2024).display()
    except InvalidDateError as e:
        print(f"  ERROR: {e}")

    print("\n  -- Testing non-leap year (Feb 29, 2023) --")
    try:
        Date(29, 2, 2023).display()
    except InvalidDateError as e:
        print(f"  ERROR caught correctly: {e}")


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------
MENU_OPTIONS = {
    "1": ("Person and Athlete (custom exceptions)", exercise_01),
    "2": ("Date class with validation",             exercise_02),
    "0": ("Exit", make_exit("Bulletin 10 — Exceptions")),
}


def bulletin_menu_10():
    run_menu("Bulletin 10 — Exceptions", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_10()


# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("10", "Bulletin 10 — Exceptions", bulletin_menu_10)
