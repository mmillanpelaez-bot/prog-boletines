"""Bulletin 04 exercises: Functions, modules and exceptions"""

from math import pi

import boletines
from utils.menu import run_menu, make_exit


# ---------------------------------------------------------------------------
# 01. Product classifier by annual sales
# ---------------------------------------------------------------------------
def exercise_01():
    """Classify a product based on its annual sales volume."""

    print("\n--- Exercise 01: Product classifier ---")

    product_name  = input("Product name:   ")
    annual_sales  = int(input("Annual sales:   "))

    # Classification thresholds defined by the problem statement
    if annual_sales <= 100:
        category = "low"
    elif annual_sales <= 500:
        category = "medium"
    elif annual_sales <= 1000:
        category = "high"
    else:
        category = "essential"  # primera necesidad

    print(f"Product '{product_name}' is classified as: {category}")


# ---------------------------------------------------------------------------
# 02. Geometric area calculator
# ---------------------------------------------------------------------------
def exercise_02():
    """Interactive sub-menu to calculate the area of rectangle, triangle or circle."""

    print("\n--- Exercise 02: Geometric area calculator ---")

    while True:
        print("\n  1. Rectangle")
        print("  2. Triangle")
        print("  3. Circle")
        print("  4. Back")

        option = input("Select a shape: ")

        if option == "1":
            def rectangle_area() -> None:
                """Area = length × width"""
                length = float(input("Length: "))
                width  = float(input("Width:  "))
                print(f"Rectangle area: {length * width}")
            rectangle_area()

        elif option == "2":
            def triangle_area() -> None:
                """Area = base × height / 2"""
                base   = float(input("Base:   "))
                height = float(input("Height: "))
                print(f"Triangle area: {base * height / 2}")
            triangle_area()

        elif option == "3":
            def circle_area() -> None:
                """Area = π × radius²"""
                radius = float(input("Radius: "))
                print(f"Circle area: {pi * radius ** 2:.4f}")
            circle_area()

        elif option == "4":
            break  # Return to the main bulletin menu

        else:
            print("ERROR: Please select a valid option.")


# ---------------------------------------------------------------------------
# 03. Absolute value using ternary operator
# ---------------------------------------------------------------------------
def exercise_03():
    """Calculate the absolute value of a number using the ternary (conditional) operator."""

    print("\n--- Exercise 03: Absolute value (ternary operator) ---")

    number = float(input("Enter a number: "))

    # Ternary: value_if_true if condition else value_if_false
    # Equivalent to abs(number) but written explicitly as required
    absolute_value = number if number >= 0 else -number

    print(f"|{number:g}| = {absolute_value:g}")


# ---------------------------------------------------------------------------
# 04. Number to words (1–99)
# ---------------------------------------------------------------------------
def exercise_04():
    """
    Ask the user for a number between 1 and 99 and display it in words.
    Example: 56 → 'fifty and six'
    """

    print("\n--- Exercise 04: Number to words (1–99) ---")

    # Lookup tables for the three groups of numbers
    units = {
        0: "zero",    1: "one",     2: "two",    3: "three",
        4: "four",    5: "five",    6: "six",    7: "seven",
        8: "eight",   9: "nine",
    }
    tens = {
        1: "ten",      2: "twenty",  3: "thirty",  4: "forty",
        5: "fifty",    6: "sixty",   7: "seventy", 8: "eighty",
        9: "ninety",
    }
    # Numbers with irregular forms that do not follow the regular tens + units pattern
    special_cases = {
        11: "eleven",      12: "twelve",     13: "thirteen",
        14: "fourteen",    15: "fifteen",    16: "sixteen",
        17: "seventeen",   18: "eighteen",   19: "nineteen",
        21: "twenty-one",  22: "twenty-two", 23: "twenty-three",
        24: "twenty-four", 25: "twenty-five",26: "twenty-six",
        27: "twenty-seven",28: "twenty-eight",29: "twenty-nine",
    }

    while True:
        user_input = input("\nEnter a number 1–99 (or press Enter to exit): ")

        if user_input == "":
            print("Goodbye!")
            break

        try:
            number = int(user_input)
            if not (1 <= number <= 99):
                print("ERROR: Number must be between 1 and 99.")
                continue
        except ValueError:
            print("ERROR: Please enter a whole number.")
            continue

        tens_digit  = number // 10  # Integer division extracts the tens digit
        units_digit = number % 10   # Modulo extracts the units digit

        # Select the correct word form based on the number's structure
        if number in special_cases:
            print(special_cases[number])
        elif number < 10:
            print(units[units_digit])
        elif units_digit == 0:
            print(tens[tens_digit])
        else:
            print(f"{tens[tens_digit]} and {units[units_digit]}")


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

MENU_OPTIONS = {
    "1": ("Product classifier",             exercise_01),
    "2": ("Geometric area calculator",      exercise_02),
    "3": ("Absolute value (ternary)",       exercise_03),
    "4": ("Number to words (1–99)",         exercise_04),
    "0": ("Exit", make_exit("Bulletin 04 — Advanced Conditionals")),
}


def bulletin_menu_04() -> None:
    """Entry point for Bulletin 04. Delegates menu logic to run_menu (utils/menu.py)."""
    run_menu("Bulletin 04 — Advanced Conditionals", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_04()


# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("4", "Bulletin 04 — Advanced Conditionals", bulletin_menu_04)