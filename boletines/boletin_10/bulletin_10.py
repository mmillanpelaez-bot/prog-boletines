"""Bulletin 10 exercises: Exceptions"""

import boletines
from utils.menu import run_menu, make_exit


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
    pass  # TODO


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
    pass  # TODO


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

MENU_OPTIONS = {
    "1": ("Persoa / Deportista with exceptions",  exercise_01),
    "2": ("Data class with validation",           exercise_02),
    "0": ("Exit", make_exit("Bulletin 10 — Exceptions")),
}


def bulletin_menu_10() -> None:
    """Entry point for Bulletin 10. Delegates menu logic to run_menu (utils/menu.py)."""
    run_menu("Bulletin 10 — Exceptions", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_10()


# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("10", "Bulletin 10 — Exceptions", bulletin_menu_10)