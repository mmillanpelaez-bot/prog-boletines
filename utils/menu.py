"""
utils/menu.py
─────────────
Generic interactive menu shared by all bulletins.

The Dispatcher pattern:
  1. Print all options from the dict.
  2. Read user input.
  3. Look up the matching function and call it.
  4. Stop the loop when any function returns False.

One place to change → change propagates to all bulletins automatically.
"""


def run_menu(title: str, options: dict) -> None:
    """
    Run an interactive menu loop.

    Parameters
    ----------
    title   : str
        Header shown above the option list. E.g. "Bulletin 05 — Loops"

    options : dict
        { "key": ("Description", function_reference) }
        Convention: key "0" paired with a function that returns False = exit.
    """
    running = True

    while running:
        print(f"\n--- {title} ---")

        for key, (description, _) in options.items():
            print(f"  {key:>2}. {description}")

        choice = input("\n>> Select an option: ")

        if choice not in options:
            print("❌ Invalid option. Please try again.")
            continue

        action = options[choice][1]

        try:
            result = action()

            if result is False:
                running = False
            else:
                input("\n[Press Enter to continue...]")

        except Exception as error:
            print(f"⚠️  Unexpected error: {error}")


def make_exit(bulletin_name: str):
    """
    Factory that returns a ready-made exit function for a bulletin menu.

    Eliminates the boilerplate of defining an identical exit_menu() in
    every bulletin. The returned function prints a farewell message and
    returns False, which signals run_menu() to stop its loop.

    Parameters
    ----------
    bulletin_name : str
        Human-readable name shown in the goodbye message.
        E.g. "Bulletin 01 — Expressions & Booleans"

    Usage
    -----
        MENU_OPTIONS = {
            "1": ("Some exercise", exercise_01),
            "0": ("Exit", make_exit("Bulletin 01 — Expressions & Booleans")),
        }
    """
    def _exit() -> bool:
        print(f"\n👋 Exiting {bulletin_name}...")
        return False
    return _exit
