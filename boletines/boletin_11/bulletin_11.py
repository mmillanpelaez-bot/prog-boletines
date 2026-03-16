"""Bulletin 11 — File I/O"""

import boletines
from utils.menu import run_menu, make_exit
from boletines.boletin_11 import notes_manager, word_counter, task_manager, customer_manager, inventory_manager, contact_book


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


boletines.register("11", "Bulletin 11 — File I/O", bulletin_menu_11)