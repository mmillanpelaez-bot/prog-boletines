"""
main.py
───────
Entry point for PROG-Boletines.

How bulletin discovery works
─────────────────────────────
1. importlib scans boletines/ for subdirectories named boletinN.
2. It imports the bulletin_NN.py file inside each one.
3. That import triggers the register() call at the bottom of each bulletin,
   which adds it to boletines.REGISTRY.
4. main_menu() reads REGISTRY to build its option list — no manual entries needed.

To add Bulletin 13:
  → Create boletines/boletin13/bulletin_13.py and call register() at the bottom.
  → Nothing else needs to change.
"""

import importlib
import os
import pkgutil

import boletines
from utils.menu import run_menu


# ---------------------------------------------------------------------------
# Auto-discovery: import every bulletin_NN module so register() fires
# ---------------------------------------------------------------------------

def _discover_bulletins() -> None:
    """
    Walk the boletines/ package and import every bulletin_NN.py module.

    pkgutil.iter_modules returns one entry per sub-package (boletin1, boletin2…).
    For each one we try to import 'boletines.boletinN.bulletin_NN'.
    Modules that don't follow the naming convention are silently skipped.
    """
    boletines_path = os.path.dirname(boletines.__file__)

    for _, package_name, is_pkg in pkgutil.iter_modules([boletines_path]):
        if not is_pkg:
            continue  # Skip plain .py files at the top level

        # Derive module name from folder name:
        # "boletin_01"  → "bulletin_01"
        # "boletin_12" → "bulletin_12"
        number = "".join(filter(str.isdigit, package_name))
        if not number:
            continue

        module_name = f"boletines.{package_name}.bulletin_{int(number):02d}"

        try:
            importlib.import_module(module_name)
        except ModuleNotFoundError:
            pass  # Bulletin exists as a folder but has no file yet — skip quietly


# ---------------------------------------------------------------------------
# Exit action
# ---------------------------------------------------------------------------

def exit_menu() -> bool:
    """Signal the main menu loop to stop by returning False."""
    print("\n👋 Goodbye!")
    return False


# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------

def main_menu() -> None:
    """
    Display the bulletin selector and handle navigation.

    MENU_OPTIONS is built from the auto-discovered REGISTRY, with the
    exit option appended at the end.
    """
    _discover_bulletins()

    # Build options from whatever got registered, sorted by key
    # Sort numerically (not lexicographically) so "10" comes after "9", not after "1"
    menu_options = dict(sorted(boletines.REGISTRY.items(), key=lambda item: int(item[0])))
    menu_options["0"] = ("Exit", exit_menu)  # Always last

    run_menu("PROG-Boletines — DAM1  |  Felipe Millán", menu_options)


if __name__ == "__main__":
    main_menu()