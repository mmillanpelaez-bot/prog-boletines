"""Bulletin 11 exercises: File I/O in Python"""

import boletines
from utils.menu import run_menu


# ---------------------------------------------------------------------------
# 01. Personal note manager
# ---------------------------------------------------------------------------
def exercise_01():
    """
    Personal note manager:
      - Add a new note (free text)
      - Save notes to notas.txt (one per line)
      - List all saved notes
      - Search notes by keyword
    """
    pass  # TODO


# ---------------------------------------------------------------------------
# 02. Word frequency counter
# ---------------------------------------------------------------------------
def exercise_02():
    """
    Read a .txt file and count word occurrences:
      - Prompt for filename
      - Display frequency (case-insensitive, punctuation stripped)
      - Save summary to resumo_palabras.txt
    """
    pass  # TODO


# ---------------------------------------------------------------------------
# 03. Task manager
# ---------------------------------------------------------------------------
def exercise_03():
    """
    Task manager with class Tarefa (date, time, duration, name, description, status).
    Operations: add, delete, update, list.
    Persistence: binary file tarefas.dat.
    """
    pass  # TODO


# ---------------------------------------------------------------------------
# 04. Customer manager
# ---------------------------------------------------------------------------
def exercise_04():
    """
    Class Cliente with id, name, phone.
    Menu: add, update, remove, list.
    Load on start, save on exit to binary file.
    """
    pass  # TODO


# ---------------------------------------------------------------------------
# 05. CSV inventory manager
# ---------------------------------------------------------------------------
def exercise_05():
    """
    Inventory management over produtos.csv (id, name, price, stock):
      - Compute total inventory value (price × stock)
      - Export products with stock < 5 to baixo_stock.csv
    """
    pass  # TODO


# ---------------------------------------------------------------------------
# 06. JSON contact book
# ---------------------------------------------------------------------------
def exercise_06():
    """
    Contact book (multiple phones + email) stored in axenda.json:
      - Add contacts
      - Save to axenda.json on exit
      - Load existing data on start
    """
    pass  # TODO


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

def exit_menu():
    """Signal the menu loop to stop by returning False."""
    print("\n👋 Exiting Bulletin 11...")
    return False


MENU_OPTIONS = {
    "1": ("Personal note manager",     exercise_01),
    "2": ("Word frequency counter",    exercise_02),
    "3": ("Task manager",              exercise_03),
    "4": ("Customer manager",          exercise_04),
    "5": ("CSV inventory manager",     exercise_05),
    "6": ("JSON contact book",         exercise_06),
    "0": ("Exit",                      exit_menu),
}


def bulletin_menu_11():
    """Entry point for Bulletin 11. Delegates menu logic to run_menu (utils/menu.py)."""
    run_menu("Bulletin 11 — File I/O", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_11()


# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("11", "Bulletin 11 — File IO", bulletin_menu_11)