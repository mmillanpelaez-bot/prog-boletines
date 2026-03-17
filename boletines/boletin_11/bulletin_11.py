"""Bulletin 11 — File I/O"""

import boletines
from utils.menu import run_menu, make_exit
from boletines.boletin_11 import notes_manager, word_counter, task_manager, customer_manager, inventory_manager, contact_book


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
    pass



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
    pass
 
 
# ---------------------------------------------------------------------------
# 03. Task manager
# ---------------------------------------------------------------------------
def exercise_03():
    """
    Task manager with class Tarefa (date, time, duration, name, description, status).
    Operations: add, delete, update, list.
    Persistence: binary file tarefas.dat.
    """
    pass
 
 
# ---------------------------------------------------------------------------
# 04. Customer manager
# ---------------------------------------------------------------------------
def exercise_04():
    """
    Class Cliente with id, name, phone.
    Menu: add, update, remove, list.
    Load on start, save on exit to binary file.
    """
    pass
 
 
# ---------------------------------------------------------------------------
# 05. CSV inventory manager
# ---------------------------------------------------------------------------
def exercise_05():
    """
    Inventory management over produtos.csv (id, name, price, stock):
      - Compute total inventory value (price × stock)
      - Export products with stock < 5 to baixo_stock.csv
    """
    pass
 
 
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
    pass
 
 
# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

MENU_OPTIONS = {
    "1": ("Personal note manager",  notes_manager),
    "2": ("Word frequency counter", word_counter),
    "3": ("Task manager",           task_manager),
    "4": ("Customer manager",       customer_manager),
    "5": ("CSV inventory manager",  inventory_manager),
    "6": ("JSON contact book",      contact_book),
    "0": ("Exit", make_exit("Bulletin 11 — File I/O")),
}


def bulletin_menu_11():
    run_menu("Bulletin 11 — File I/O", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_11()


# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("11", "Bulletin 11 — File I/O", bulletin_menu_11)