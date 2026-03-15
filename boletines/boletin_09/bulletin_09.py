"""Bulletin 09 exercises: Object-Oriented Python"""

import boletines
from utils.menu import run_menu


# ---------------------------------------------------------------------------
# 01. Libro class
# ---------------------------------------------------------------------------
def exercise_01():
    """
    Create class Libro with attributes: titulo, autor, ano, numPaginas, valoracion.
    Implement: __init__, getters, setters, properties, amosarLibro method.
    """
    pass  # TODO


# ---------------------------------------------------------------------------
# 02. Consumo class
# ---------------------------------------------------------------------------
def exercise_02():
    """
    Class Consumo (car electronic dashboard):
    Attributes: km, litros, vMed, pGas.
    Methods: getTempo, consumoMedio, consumoEuros, setters.
    """
    pass  # TODO


# ---------------------------------------------------------------------------
# 03. Coche and Conta classes
# ---------------------------------------------------------------------------
def exercise_03():
    """
    Class Coche: getVelocidade, acelerar(value), frenar(amount).
    Class Conta: deposit, withdrawal, transfer between accounts.
    """
    pass  # TODO


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

def exit_menu():
    """Signal the menu loop to stop by returning False."""
    print("\n👋 Exiting Bulletin 09...")
    return False


MENU_OPTIONS = {
    "1": ("Class Libro",              exercise_01),
    "2": ("Class Consumo",            exercise_02),
    "3": ("Class Coche / Conta",      exercise_03),
    "0": ("Exit",                     exit_menu),
}


def bulletin_menu_09():
    """Entry point for Bulletin 09. Delegates menu logic to run_menu (utils/menu.py)."""
    run_menu("Bulletin 09 — Object-Oriented Python", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_09()


# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("9", "Bulletin 09 — Object-Oriented Python", bulletin_menu_09)