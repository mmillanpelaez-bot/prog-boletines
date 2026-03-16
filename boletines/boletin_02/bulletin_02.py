"""Bulletin 02 exercises: Algorithmics and basic sequences"""

import requests

import boletines
from utils.menu import run_menu, make_exit

# ---------------------------------------------------------------------------
# 01. Triangle area
# ---------------------------------------------------------------------------
def exercise_01():
    """Calculate the area of a triangle. Formula: area = base × height / 2"""

    print("\n--- Exercise 01: Triangle area ---")

    base   = 4
    height = 3
    area   = base * height / 2  # Classic triangle area formula

    print(f"Base: {base}  |  Height: {height}  |  Area: {area}")


# ---------------------------------------------------------------------------
# 02. Square area
# ---------------------------------------------------------------------------
def exercise_02():
    """Calculate the area of a square. Formula: area = side²"""

    print("\n--- Exercise 02: Square area ---")

    side = 3
    area = side ** 2  # ** is the exponentiation operator in Python

    print(f"Side: {side}  |  Area: {area}")


# ---------------------------------------------------------------------------
# 03. Currency converter: EUR → USD
# ---------------------------------------------------------------------------
def exercise_03():
    """Convert euros to dollars using the live Frankfurter exchange rate API."""

    print("\n--- Exercise 03: EUR → USD converter ---")

    def get_exchange_rate() -> float:
        """
        Fetches the live EUR/USD rate from the Frankfurter API.
        Falls back to manual input if the request fails (no internet, timeout, etc.)
        """
        try:
            url      = "https://api.frankfurter.dev/v1/latest?from=EUR&to=USD"
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raises an error for 4xx/5xx responses
            return response.json()["rates"]["USD"]
        except Exception as error:
            print(f"⚠️  Could not fetch live rate. Reason: {error}")
            return float(input("Please enter the exchange rate manually (USD per EUR): "))

    exchange_rate = get_exchange_rate()
    print(f"Using EUR → USD rate: {exchange_rate:.4f}")

    eur_amount = float(input("Enter amount in euros (€): "))
    usd_amount = eur_amount * exchange_rate

    print(f"{eur_amount} € = {usd_amount:.2f} $  (rate: {exchange_rate:.4f})")


# ---------------------------------------------------------------------------
# 04. Basic arithmetic sequence (pseudocode → Python)
# ---------------------------------------------------------------------------
"""
Algorithm pseudocode:
  1. START
  2. ASK  'Enter first number: '
  3. READ num_1
  4. ASK  'Enter second number: '
  5. READ num_2
  6. COMPUTE sum     = num_1 + num_2
  7. SHOW  'sum = ' {sum}
  8. COMPUTE diff    = num_1 - num_2
  9. SHOW  'diff = ' {diff}
 10. COMPUTE product = num_1 * num_2
 11. SHOW  'product = ' {product}
     IF num_2 != 0:
 12.   COMPUTE quotient = num_1 / num_2
 13.   SHOW 'quotient = ' {quotient}
     ELSE:
       SHOW 'Cannot divide by zero'
 14. END
"""


def exercise_04():
    """Implement the arithmetic sequence described in the pseudocode above."""

    print("\n--- Exercise 04: Arithmetic sequence ---")

    num_1 = float(input("Enter the first number:  "))
    num_2 = float(input("Enter the second number: "))

    print(f"sum     = {num_1 + num_2}")
    print(f"diff    = {num_1 - num_2}")
    print(f"product = {num_1 * num_2}")

    # Guard against division by zero before computing the quotient
    if num_2 != 0:
        print(f"quotient = {num_1 / num_2}")
    else:
        print("quotient = Error: cannot divide by zero")


# ---------------------------------------------------------------------------
# 05. Nautical miles to metres
# ---------------------------------------------------------------------------
def exercise_05():
    """Convert a distance in nautical miles to metres. 1 nmi = 1852 m"""

    print("\n--- Exercise 05: Nautical miles → Metres ---")

    nautical_miles = float(input("Distance in nautical miles: "))
    meters         = nautical_miles * 1852  # Exact conversion factor

    print(f"{nautical_miles} nmi = {meters} m")


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

MENU_OPTIONS = {
    "1": ("Triangle area",                  exercise_01),
    "2": ("Square area",                    exercise_02),
    "3": ("EUR → USD converter",            exercise_03),
    "4": ("Arithmetic sequence",            exercise_04),
    "5": ("Nautical miles → Metres",        exercise_05),
    "0": ("Exit", make_exit("Bulletin 02 — Algorithmics")),
}


def bulletin_menu_02() -> None:
    """Entry point for Bulletin 02. Delegates menu logic to run_menu (utils/menu.py)."""
    run_menu("Bulletin 02 — Algorithmics", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_02()


# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("2", "Bulletin 02 — Algorithmics", bulletin_menu_02)