"""Bulletin 10 — Exceptions"""

import boletines
from utils.menu import run_menu, make_exit
from boletines.boletin_10 import athlete_main, date_main


MENU_OPTIONS = {
    "1": ("Person and Athlete (custom exceptions)", athlete_main),
    "2": ("Date class with validation",             date_main),
    "0": ("Exit", make_exit("Bulletin 10 — Exceptions")),
}


def bulletin_menu_10():
    run_menu("Bulletin 10 — Exceptions", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_10()


boletines.register("10", "Bulletin 10 — Exceptions", bulletin_menu_10)
