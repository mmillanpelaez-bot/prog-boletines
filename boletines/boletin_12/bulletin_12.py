"""Bulletin 12 exercises: (topic pending)"""

import boletines
from utils.menu import run_menu


def exit_menu():
    """Signal the menu loop to stop by returning False."""
    print("\n👋 Exiting Bulletin 12...")
    return False


MENU_OPTIONS = {
    "0": ("Exit", exit_menu),
}


def bulletin_menu_12():
    """Entry point for Bulletin 12. Delegates menu logic to run_menu (utils/menu.py)."""
    run_menu("Bulletin 12", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_12()


# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("12", "Bulletin 12 — (topic pending)", bulletin_menu_12)