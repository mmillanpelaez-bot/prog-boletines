"""Bulletin 06 exercises: Lists and tuples"""

import math

import boletines
from utils.menu import run_menu, make_exit


# ---------------------------------------------------------------------------
# 01. Store and display grades by subject
# ---------------------------------------------------------------------------
def exercise_01():
    """Ask the user for a grade per subject and display them together."""

    print("\n--- Exercise 01: Grades by subject ---")

    subjects = ["Mathematics", "Physics", "Chemistry", "History", "Language"]
    grades   = []

    # Collect one grade per subject
    for subject in subjects:
        grade = input(f"\nEnter your grade in {subject}: ")
        grades.append(grade)

    # Display subject + grade pairs using the index to keep them in sync
    for i in range(len(subjects)):
        print(f"\nIn {subjects[i]} you got {grades[i]}")


# ---------------------------------------------------------------------------
# 02. Lottery numbers sorted ascending
# ---------------------------------------------------------------------------
def exercise_02():
    """Ask for 6 unique lottery numbers (1–49) and display them sorted."""

    print("\n--- Exercise 02: Lottery numbers (sorted) ---")

    NUMBER_COUNT = 6   # Exactly 6 numbers required
    MIN_VALUE    = 1   # Minimum allowed number
    MAX_VALUE    = 49  # Maximum allowed number

    winning_numbers = []

    while len(winning_numbers) < NUMBER_COUNT:
        try:
            number = int(input(f"\nEnter number {len(winning_numbers)+1}/{NUMBER_COUNT}: "))

            if not (MIN_VALUE <= number <= MAX_VALUE):
                print(f"ERROR: Number must be between {MIN_VALUE} and {MAX_VALUE}.")
                continue

            if number in winning_numbers:
                print(f"ERROR: {number} has already been entered.")
                continue

            winning_numbers.append(number)

        except ValueError:
            print("ERROR: Invalid input — please enter a whole number.")

    winning_numbers.sort()
    print(f"\nWinning numbers (sorted): {winning_numbers}")


# ---------------------------------------------------------------------------
# 03. Numbers 1–10 reversed, comma-separated
# ---------------------------------------------------------------------------
def exercise_03():
    """Store numbers 1–10 in a list and print them in reverse, separated by commas."""

    print("\n--- Exercise 03: Reversed number list ---")

    numbers          = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    reversed_numbers = numbers[::-1]  # Slice with step -1 reverses the list

    print(", ".join(reversed_numbers))


# ---------------------------------------------------------------------------
# 04. Failed subjects
# ---------------------------------------------------------------------------
def exercise_04():
    """Ask for grades per subject and display only the failed ones (grade < 5)."""

    print("\n--- Exercise 04: Failed subjects ---")

    subjects = ["Mathematics", "Physics", "Chemistry", "History", "Language"]
    grades   = []

    for subject in subjects:
        grade = float(input(f"\nEnter your grade in {subject}: "))
        grades.append(grade)

    # Iterate in reverse to safely remove passed subjects without shifting indices
    for i in range(len(subjects) - 1, -1, -1):
        if grades[i] >= 5:
            subjects.pop(i)
            grades.pop(i)

    print("\n--- Result ---")
    if not subjects:
        print("🎉 Congratulations! You passed everything.")
    else:
        print("You need to retake the following subjects:")
        for subject in subjects:
            print(f"  - {subject}")


# ---------------------------------------------------------------------------
# 05. Alphabet excluding multiples-of-3 positions
# ---------------------------------------------------------------------------
def exercise_05():
    """
    Store the alphabet in a list and create a filtered version
    that excludes letters at positions that are multiples of 3 (0-indexed).
    """

    print("\n--- Exercise 05: Filtered alphabet ---")

    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Keep letter only if its index is NOT a multiple of 3
    filtered_alphabet = [letter for i, letter in enumerate(alphabet) if i % 3 != 0]

    # Pythonic one-liner (equivalent):
    # filtered_alphabet = [c for i, c in enumerate(alphabet) if i % 3 != 0]

    print(f"Original : {alphabet}")
    print(f"Filtered : {filtered_alphabet}")


# ---------------------------------------------------------------------------
# 06. Palindrome checker
# ---------------------------------------------------------------------------
def exercise_06():
    """Ask for a word and report whether it is a palindrome."""

    print("\n--- Exercise 06: Palindrome checker ---")

    while True:
        word = input("\nEnter a word (or press Enter to exit): ").upper()

        if word == "":
            print("Goodbye!")
            break

        if not word.isalpha():
            print("ERROR: Please enter letters only.")
            continue

        # A palindrome reads the same forwards and backwards
        if word == word[::-1]:
            print(f'"{word}" is a palindrome ✅')
        else:
            print(f'"{word}" is not a palindrome ❌')


# ---------------------------------------------------------------------------
# 07. Vowel frequency
# ---------------------------------------------------------------------------
def exercise_07():
    """Count how many times each vowel appears in a user-entered word."""

    print("\n--- Exercise 07: Vowel frequency ---")

    VOWELS = ("A", "E", "I", "O", "U")
    word   = input("Enter a word: ").upper()

    for vowel in VOWELS:
        count = word.count(vowel)  # str.count() returns the number of occurrences
        print(f"  {vowel}: {count}")


# ---------------------------------------------------------------------------
# 08. Min and max of a price list
# ---------------------------------------------------------------------------
def exercise_08():
    """Display the minimum and maximum price from a predefined list."""

    print("\n--- Exercise 08: Price range ---")

    prices = [50, 75, 46, 22, 80, 65, 8]

    # max() and min() are built-in functions — no manual loop needed
    print(f"Prices : {prices}")
    print(f"Highest: {max(prices)}")
    print(f"Lowest : {min(prices)}")


# ---------------------------------------------------------------------------
# 09. Dot product of two vectors
# ---------------------------------------------------------------------------
def exercise_09():
    """Compute the dot product of vectors (1,2,3) and (-1,0,2)."""

    print("\n--- Exercise 09: Dot product ---")

    vector_1 = [1, 2, 3]
    vector_2 = [-1, 0, 2]

    # Dot product: sum of element-wise products
    # zip() pairs corresponding elements: (1,-1), (2,0), (3,2)
    dot_product = sum(v1 * v2 for v1, v2 in zip(vector_1, vector_2))

    print(f"Vector 1    : {vector_1}")
    print(f"Vector 2    : {vector_2}")
    print(f"Dot product : {dot_product}")


# ---------------------------------------------------------------------------
# 10. Matrix multiplication
# ---------------------------------------------------------------------------
def exercise_10():
    """
    Compute the product of matrices A = [(1,2,3),(4,5,6)] and B = [(-1,0),(0,1),(1,1)].
    Each row is represented as a tuple inside a list.
    """

    print("\n--- Exercise 10: Matrix multiplication ---")

    matrix_a = [(1, 2, 3), (4, 5, 6)]
    matrix_b = [(-1, 0), (0, 1), (1, 1)]

    # Nested list comprehension for matrix multiplication:
    # result[i][j] = sum of row_a[k] × col_b[k]  for each k
    # zip(*matrix_b) transposes B so we can iterate over its columns
    result = [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*matrix_b)]
        for row_a in matrix_a
    ]

    print(f"Matrix A : {matrix_a}")
    print(f"Matrix B : {matrix_b}")
    print("A × B    :")
    for row in result:
        print(f"  {row}")


# ---------------------------------------------------------------------------
# 11. Mean and standard deviation
# ---------------------------------------------------------------------------
def exercise_11():
    """Read a comma-separated list of numbers and compute their mean and standard deviation."""

    print("\n--- Exercise 11: Mean and standard deviation ---")

    raw_input = input("Enter numbers separated by commas: ")

    # Strip whitespace around each token before converting
    numbers = [float(x.strip()) for x in raw_input.split(",")]

    mean = sum(numbers) / len(numbers)

    # Population standard deviation: σ = √( Σ(xᵢ - μ)² / n )
    variance  = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev   = math.sqrt(variance)

    print(f"\nNumbers          : {numbers}")
    print(f"Mean             : {mean:.2f}")
    print(f"Standard deviation: {std_dev:.2f}")


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

MENU_OPTIONS = {
    "1" : ("Grades by subject",                    exercise_01),
    "2" : ("Lottery numbers (sorted)",             exercise_02),
    "3" : ("Reversed number list",                 exercise_03),
    "4" : ("Failed subjects",                      exercise_04),
    "5" : ("Filtered alphabet",                    exercise_05),
    "6" : ("Palindrome checker",                   exercise_06),
    "7" : ("Vowel frequency",                      exercise_07),
    "8" : ("Price range (min/max)",                exercise_08),
    "9" : ("Dot product",                          exercise_09),
    "10": ("Matrix multiplication",                exercise_10),
    "11": ("Mean and standard deviation",          exercise_11),
    "0" : ("Exit", make_exit("Bulletin 06 — Lists & Tuples")),
}


def bulletin_menu_06() -> None:
    """Entry point for Bulletin 06. Delegates menu logic to run_menu (utils/menu.py)."""
    run_menu("Bulletin 06 — Lists & Tuples", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_06()


# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("6", "Bulletin 06 — Lists and Tuples", bulletin_menu_06)
