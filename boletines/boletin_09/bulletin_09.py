"""Bulletin 09 — Object-Oriented Python"""

import boletines
from utils.menu import run_menu, make_exit
from boletines.boletin_09 import book_main, fuel_consumption_main, bank_account_main


MENU_OPTIONS = {
    "1": ("Book class",                    book_main),
    "2": ("Fuel Consumption class",        fuel_consumption_main),
    "3": ("Car and BankAccount classes",   bank_account_main),
    "0": ("Exit", make_exit("Bulletin 09 — Object-Oriented Python")),
}


def bulletin_menu_09():
    run_menu("Bulletin 09 — Object-Oriented Python", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_09()


boletines.register("9", "Bulletin 09 — Object-Oriented Python", bulletin_menu_09)
