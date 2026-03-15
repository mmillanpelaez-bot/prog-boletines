"""
utils/menu.py
─────────────
Generic interactive menu shared by all bulletins.

The Dispatcher pattern:
  1. Print all options from the dict.
  2. Read user input.
  3. Look up the matching function and call it.
  4. Stop the loop when any function returns False.

One place to change → change propagates to all 12 bulletins automatically.
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

        # Build the list dynamically from the dict.
        # Adding an entry to MENU_OPTIONS is all that's needed to show it here.
        for key, (description, _) in options.items():
            print(f"  {key:>2}. {description}")

        choice = input("\n>> Select an option: ")

        # Guard clause: reject invalid input before doing anything else.
        # Keeps the happy path at the left margin (no nested else needed).
        if choice not in options:
            print("❌ Invalid option. Please try again.")
            continue

        action = options[choice][1]  # Retrieve function reference (not yet called)

        try:
            result = action()  # Call the function

            # Convention: returning False signals "exit this menu"
            if result is False:
                running = False
            else:
                input("\n[Press Enter to continue...]")

        except Exception as error:
            # Catch errors inside an exercise so the menu keeps running
            print(f"⚠️  Unexpected error: {error}")