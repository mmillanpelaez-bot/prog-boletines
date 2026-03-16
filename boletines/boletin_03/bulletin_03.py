"""Bulletin 03 exercises: Control structures and conditionals"""

import boletines
from utils.menu import run_menu, make_exit

# ---------------------------------------------------------------------------
# 01. Natural number checker
# ---------------------------------------------------------------------------
def exercise_01():
    """Ask the user for a number and report whether it is positive or not."""

    print("\n--- Exercise 01: Natural number checker ---")

    # Validation loop: repeat until a valid number is entered
    while True:
        try:
            number = float(input("\nEnter a number: "))
            break
        except ValueError:
            print("ERROR: That is not a valid number.")

    if number >= 0:
        print(f"{number} is a positive number.")
    else:
        print(f"{number} is not a positive number.")


# ---------------------------------------------------------------------------
# 02. Subtraction and sum of two numbers
# ---------------------------------------------------------------------------
def exercise_02():
    """
    Given two numbers: show the subtraction if the first >= second,
    then always show the sum.
    """

    print("\n--- Exercise 02: Subtraction and sum ---")

    while True:
        try:
            num_1 = float(input("\nEnter the first number:  "))
            num_2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("ERROR: That is not a valid number.")

    # Subtraction is only shown when the first number is greater or equal
    if num_1 >= num_2:
        print(f"Subtraction: {num_1} - {num_2} = {num_1 - num_2}")

    # Sum is always shown regardless of the comparison above
    print(f"Sum: {num_1} + {num_2} = {num_1 + num_2}")


# ---------------------------------------------------------------------------
# 03. Sign indicator
# ---------------------------------------------------------------------------
def exercise_03():
    """Show '+', '-' or '0' depending on the sign of the entered number."""

    print("\n--- Exercise 03: Sign indicator ---")

    while True:
        try:
            number = float(input("\nEnter a number: "))
            break
        except ValueError:
            print("ERROR: That is not a valid number.")

    # Three mutually exclusive cases cover all real numbers
    if number > 0:
        print("+")
    elif number == 0:
        print("0")
    else:
        print("-")


# ---------------------------------------------------------------------------
# 04. Compare weights of two people
# ---------------------------------------------------------------------------
def exercise_04():
    """Given the name and weight of two people, print who weighs more and by how much."""

    print("\n--- Exercise 04: Weight comparison ---")

    name_1 = input("Name of the first person:  ")
    name_2 = input("Name of the second person: ")

    weight_1 = float(input(f"How much does {name_1} weigh (kg)? "))
    weight_2 = float(input(f"How much does {name_2} weigh (kg)? "))

    if weight_1 > weight_2:
        print(f"{name_1} weighs {weight_1 - weight_2:.2f} kg more than {name_2}.")
    elif weight_2 > weight_1:
        print(f"{name_2} weighs {weight_2 - weight_1:.2f} kg more than {name_1}.")
    else:
        print(f"{name_1} and {name_2} weigh the same: {weight_1} kg.")


# ---------------------------------------------------------------------------
# 05. Greatest of three numbers
# ---------------------------------------------------------------------------
def exercise_05():
    """Given three distinct numbers, print the greatest one."""

    print("\n--- Exercise 05: Greatest of three numbers ---")

    num_1 = float(input("Enter the first number:  "))
    num_2 = float(input("Enter the second number: "))
    num_3 = float(input("Enter the third number:  "))

    # max() is the idiomatic Python way; the nested-if approach is shown commented below
    greatest = max(num_1, num_2, num_3)
    print(f"The greatest number is: {greatest}")

    # Alternative with nested if (equivalent, more explicit):
    # if num_1 > num_2 and num_1 > num_3:
    #     print(num_1)
    # elif num_2 > num_3:
    #     print(num_2)
    # else:
    #     print(num_3)


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

MENU_OPTIONS = {
    "1": ("Natural number checker",         exercise_01),
    "2": ("Subtraction and sum",            exercise_02),
    "3": ("Sign indicator",                 exercise_03),
    "4": ("Weight comparison",              exercise_04),
    "5": ("Greatest of three numbers",      exercise_05),
    "0": ("Exit", make_exit("Bulletin 03 — Conditionals")),
}


def bulletin_menu_03() -> None:
    """Entry point for Bulletin 03. Delegates menu logic to run_menu (utils/menu.py)."""
    run_menu("Bulletin 03 — Conditionals", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_03()


# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("3", "Bulletin 03 — Conditionals", bulletin_menu_03)