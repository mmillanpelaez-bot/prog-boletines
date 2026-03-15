"""Bulletin 05 exercises: Loops and iterative structures"""

import boletines
from utils.menu import run_menu


# ---------------------------------------------------------------------------
# 01. Print numbers 10 to 20
# ---------------------------------------------------------------------------
def exercise_01():
    """Print all numbers from 10 to 20 using a definite loop."""

    print("\n--- Exercise 01: Numbers from 10 to 20 ---")

    # range(10, 21) → upper bound is exclusive, so 21 is needed to reach 20
    for number in range(10, 21):
        print(number)


# ---------------------------------------------------------------------------
# 02. Fahrenheit to Celsius converter
# ---------------------------------------------------------------------------
def exercise_02():
    """Convert a user-entered Fahrenheit temperature to Celsius. F = 9/5·C + 32"""

    print("\n--- Exercise 02: Fahrenheit → Celsius ---")

    def fahrenheit_to_celsius(degrees_f: float) -> float:
        """
        Converts Fahrenheit to Celsius.
        Formula rearranged: C = (F - 32) × 5/9
        """
        return (degrees_f - 32) * 5 / 9

    # Repeat until a valid number is entered
    while True:
        try:
            temperature = float(input("Enter temperature in °F: "))
            print(f"= {fahrenheit_to_celsius(temperature):.2f} °C")
            break
        except ValueError:
            print("ERROR: Please enter a valid number.")


# ---------------------------------------------------------------------------
# 03. Temperature conversion table (0–120 °F, step 10)
# ---------------------------------------------------------------------------
def exercise_03():
    """Generate a Fahrenheit to Celsius conversion table from 0 to 120 °F."""

    print("\n--- Exercise 03: Temperature conversion table ---")

    # Right-aligned column headers for readability
    print(f"{'Fahrenheit':>12} | {'Celsius':>10}")
    print("-" * 27)

    # range step of 10 → 13 rows from 0 to 120 inclusive
    for degrees_f in range(0, 121, 10):
        degrees_c = (degrees_f - 32) * 5 / 9
        print(f"{degrees_f:>10} °F | {degrees_c:>8.2f} °C")


# ---------------------------------------------------------------------------
# 04. Even numbers between two values
# ---------------------------------------------------------------------------
def exercise_04():
    """Print all even numbers between two user-entered integers."""

    print("\n--- Exercise 04: Even numbers between two values ---")

    while True:
        try:
            start = int(input("Start value: "))
            end   = int(input("End value:   "))
            # Swap silently if the user enters them in reverse order
            if start > end:
                start, end = end, start
            break
        except ValueError:
            print("ERROR: Please enter whole numbers.")

    # n % 2 == 0 filters even numbers; end + 1 includes the upper bound
    even_numbers = [n for n in range(start, end + 1) if n % 2 == 0]
    print(f"Even numbers between {start} and {end}: {even_numbers}")


# ---------------------------------------------------------------------------
# 05. First n triangular numbers
# ---------------------------------------------------------------------------
def exercise_05():
    """
    Print the first n triangular numbers alongside their index.
    T(n) = 1 + 2 + ... + n = n·(n+1)/2
    """

    print("\n--- Exercise 05: First n triangular numbers ---")

    while True:
        try:
            n = int(input("How many triangular numbers? "))
            if n > 0:
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("ERROR: Please enter a whole number.")

    # Without formula: cumulative sum — performs n additions
    print("\n  i  |  Without formula (cumulative sum)")
    print("-" * 38)
    accumulated = 0
    for i in range(1, n + 1):
        accumulated += i
        print(f"  {i:<4}|  {accumulated}")

    # With formula: n·(n+1)//2 — always 2 operations, more efficient
    print("\n  i  |  With formula n·(n+1)/2")
    print("-" * 30)
    for i in range(1, n + 1):
        triangular = i * (i + 1) // 2
        print(f"  {i:<4}|  {triangular}")


# ---------------------------------------------------------------------------
# 06. Factorial of m numbers
# ---------------------------------------------------------------------------
def exercise_06():
    """Ask for m numbers, compute the factorial of each, and print with its order."""

    print("\n--- Exercise 06: Factorials ---")

    while True:
        try:
            count = int(input("How many numbers? "))
            if count > 0:
                break
        except ValueError:
            pass
        print("Please enter a positive whole number.")

    for order in range(1, count + 1):
        # Each number must be a non-negative integer (0! = 1 is valid)
        while True:
            try:
                number = int(input(f"  Number {order}: "))
                if number >= 0:
                    break
                print("  Please enter a non-negative integer.")
            except ValueError:
                print("  ERROR: Invalid value.")

        # factorial(n) = 1 × 2 × 3 × ... × n  (start at 2 since ×1 is a no-op)
        factorial = 1
        for i in range(2, number + 1):
            factorial *= i

        print(f"  {order}. {number}! = {factorial}")


# ---------------------------------------------------------------------------
# 07. Domino tiles (0–6)
# ---------------------------------------------------------------------------
def exercise_07():
    """Print all domino tiles from [0|0] to [6|6] without duplicates."""

    print("\n--- Exercise 07: Domino tiles (0–6) ---")

    # second starts at first to avoid printing [1|3] when [3|1] already exists
    for first in range(7):
        for second in range(first, 7):
            print(f"[{first}|{second}]", end="  ")
        print()  # newline after each row


# ---------------------------------------------------------------------------
# 08. Custom domino tiles (0–n)
# ---------------------------------------------------------------------------
def exercise_08():
    """Generate domino tiles for a game with numbers from 0 to a custom maximum."""

    print("\n--- Exercise 08: Custom domino tiles ---")

    while True:
        try:
            max_value = int(input("Maximum tile value: "))
            if max_value >= 0:
                break
        except ValueError:
            pass
        print("Please enter a non-negative integer.")

    # Same pattern as exercise_07 but using max_value as the upper bound
    for first in range(max_value + 1):
        for second in range(first, max_value + 1):
            print(f"[{first}|{second}]", end="  ")
        print()


# ---------------------------------------------------------------------------
# 09. Classify 10 numbers: positives / negatives / zeros
# ---------------------------------------------------------------------------
def exercise_09():
    """Count how many of 10 entered integers are positive, negative or zero."""

    print("\n--- Exercise 09: Number classifier (10 inputs) ---")

    # Three counters for the three possible categories
    positives = 0
    negatives = 0
    zeros     = 0

    for i in range(1, 11):
        while True:
            try:
                number = int(input(f"  Number {i:>2}/10: "))
                break
            except ValueError:
                print("  Please enter a whole number.")

        # Classify by sign
        if number > 0:
            positives += 1
        elif number < 0:
            negatives += 1
        else:
            zeros += 1

    print(f"\nPositives: {positives}  |  Negatives: {negatives}  |  Zeros: {zeros}")


# ---------------------------------------------------------------------------
# 10. Rectangle area with validated input
# ---------------------------------------------------------------------------
def exercise_10():
    """Calculate the rectangle area, rejecting non-positive values."""

    print("\n--- Exercise 10: Rectangle area (with validation) ---")

    # Validation loop: reject negatives, zeros and non-numbers
    while True:
        try:
            base   = float(input("Base   (> 0): "))
            height = float(input("Height (> 0): "))
            if base > 0 and height > 0:
                break
            print("Both values must be positive.")
        except ValueError:
            print("ERROR: Please enter valid numbers.")

    area = base * height
    print(f"Area = {base} × {height} = {area:.2f}")


# ---------------------------------------------------------------------------
# 11. Multiplication table (until user enters 0)
# ---------------------------------------------------------------------------
def exercise_11():
    """Print the multiplication table of any number. Stops when the user enters 0."""

    print("\n--- Exercise 11: Multiplication table ---")

    while True:
        try:
            number = int(input("\nEnter a number (0 to exit): "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if number == 0:
            break  # 0 is the exit condition

        print(f"\n  Table of {number}")
        print("  " + "-" * 20)

        # Multiply from 1 to 10
        for multiplier in range(1, 11):
            print(f"  {number} × {multiplier:>2} = {number * multiplier:>4}")


# ---------------------------------------------------------------------------
# 12. Salary analysis
# ---------------------------------------------------------------------------
def exercise_12():
    """
    Read worker salaries (0 to stop) and report:
    - how many earn between 1000 and 1750 €
    - percentage earning less than 1000 €
    """

    print("\n--- Exercise 12: Salary analysis ---")
    print("Enter salaries (0 to stop, negatives are rejected)\n")

    total_workers  = 0  # Total workers processed
    mid_range      = 0  # Earn between 1000 and 1750 € (both inclusive)
    below_thousand = 0  # Earn less than 1000 €

    while True:
        try:
            salary = float(input("Salary: "))
        except ValueError:
            print("Invalid value.")
            continue

        if salary == 0:
            break  # Stop condition

        if salary < 0:
            print("Salaries cannot be negative.")
            continue

        total_workers += 1

        if 1000 <= salary <= 1750:
            mid_range += 1
        if salary < 1000:
            below_thousand += 1

    if total_workers == 0:
        print("No data entered.")
        return

    # Percentage relative to the total number of workers
    percentage_below = (below_thousand / total_workers) * 100

    print(f"\nWorkers recorded        : {total_workers}")
    print(f"Earn 1000–1750 €        : {mid_range}")
    print(f"Percentage below 1000 € : {percentage_below:.1f}%")


# ---------------------------------------------------------------------------
# 13. Asterisk triangle
# ---------------------------------------------------------------------------
def exercise_13():
    """
    Draw a right-aligned triangle of asterisks with base and height n.
    Example for n = 4:
           *
          * *
         * * *
        * * * *
    """

    print("\n--- Exercise 13: Asterisk triangle ---")

    while True:
        try:
            height = int(input("Height/base of the triangle: "))
            if height > 0:
                break
        except ValueError:
            pass
        print("Please enter a positive whole number.")

    # Row i: (height - i) leading spaces + i asterisks separated by spaces
    for row in range(1, height + 1):
        indentation = " " * (height - row)
        stars       = "* " * row
        print(indentation + stars)


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

def exit_menu():
    """Signal the menu loop to stop by returning False."""
    print("\n👋 Exiting Bulletin 05...")
    return False


MENU_OPTIONS = {
    "1" : ("Numbers from 10 to 20",                exercise_01),
    "2" : ("Fahrenheit → Celsius",                 exercise_02),
    "3" : ("Temperature conversion table",         exercise_03),
    "4" : ("Even numbers between two values",      exercise_04),
    "5" : ("First n triangular numbers",           exercise_05),
    "6" : ("Factorial of m numbers",               exercise_06),
    "7" : ("Domino tiles (0–6)",                   exercise_07),
    "8" : ("Custom domino tiles",                  exercise_08),
    "9" : ("Number classifier (10 inputs)",        exercise_09),
    "10": ("Rectangle area (with validation)",     exercise_10),
    "11": ("Multiplication table",                 exercise_11),
    "12": ("Salary analysis",                      exercise_12),
    "13": ("Asterisk triangle",                    exercise_13),
    "0" : ("Exit",                                 exit_menu),
}


def bulletin_menu_05():
    """Entry point for Bulletin 05. Delegates menu logic to run_menu (utils/menu.py)."""
    run_menu("Bulletin 05 — Loops", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_05()


# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("5", "Bulletin 05 — Loops", bulletin_menu_05)