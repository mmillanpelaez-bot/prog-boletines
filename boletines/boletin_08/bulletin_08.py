"""Bulletin 08 exercises: Tuples and lists (advanced)"""

import boletines
from utils.menu import run_menu, make_exit


# ---------------------------------------------------------------------------
# 01. Is a tuple sorted ascending?
# ---------------------------------------------------------------------------
def exercise_01():
    """Check whether the elements of a tuple are in ascending order."""

    print("\n--- Exercise 01: Is tuple sorted ascending? ---")

    def is_sorted(t: tuple) -> bool:
        """
        Returns True if every element is ≤ the next one.
        all() short-circuits: stops as soon as a False is found.
        """
        return all(t[i] <= t[i + 1] for i in range(len(t) - 1))

    raw_input = input("Enter numbers separated by commas: ")
    try:
        data = tuple(float(x.strip()) for x in raw_input.split(","))
    except ValueError:
        print("ERROR: Numbers only.")
        return

    if is_sorted(data):
        print(f"✅ {data} IS sorted ascending.")
    else:
        print(f"❌ {data} is NOT sorted ascending.")


# ---------------------------------------------------------------------------
# 02. Do two domino tiles match?
# ---------------------------------------------------------------------------
def exercise_02():
    """Report whether two domino tiles share a number (and therefore can be played together)."""

    print("\n--- Exercise 02: Do domino tiles match? ---")

    def tiles_match(tile_1: tuple, tile_2: tuple) -> bool:
        """
        Two tiles match if their number sets intersect.
        Set intersection (&) runs in O(min(len(a), len(b))).
        """
        return bool(set(tile_1) & set(tile_2))

    try:
        a, b = map(int, input("Tile 1 (e.g. 3 4): ").split())
        c, d = map(int, input("Tile 2 (e.g. 5 4): ").split())
    except ValueError:
        print("ERROR: Enter two integers per tile.")
        return

    tile_1 = (a, b)
    tile_2 = (c, d)

    if tiles_match(tile_1, tile_2):
        print(f"✅ {tile_1} and {tile_2} match.")
    else:
        print(f"❌ {tile_1} and {tile_2} do NOT match.")


# ---------------------------------------------------------------------------
# 03. Formal greetings from a name tuple
# ---------------------------------------------------------------------------
def exercise_03():
    """Print 'Dear Mr/Ms Name' for each name in a predefined tuple."""

    print("\n--- Exercise 03: Formal greetings ---")

    def greet_all(names: tuple) -> None:
        for name in names:
            print(f"Dear Mr/Ms {name}")

    names = ("Ana", "Carlos", "María", "Xoán", "Laura")
    print(f"Names: {names}\n")
    greet_all(names)


# ---------------------------------------------------------------------------
# 04. Greetings for n names starting at position p
# ---------------------------------------------------------------------------
def exercise_04():
    """Print greetings for n names from the tuple, starting at index p."""

    print("\n--- Exercise 04: Greetings from position p, n items ---")

    def greet_range(names: tuple, start: int, count: int) -> None:
        """
        names[start : start + count] — slicing never raises IndexError,
        it just returns fewer items if the range exceeds the list length.
        """
        for name in names[start: start + count]:
            print(f"Dear Mr/Ms {name}")

    names = ("Ana", "Carlos", "María", "Xoán", "Laura", "Pedro", "Sofía")
    print(f"Available names: {names}")

    try:
        start_pos = int(input("Start position (p): "))
        count     = int(input("Count (n):          "))
    except ValueError:
        print("ERROR: Please enter integers.")
        return

    greet_range(names, start_pos, count)


# ---------------------------------------------------------------------------
# 05. Gender-aware greetings
# ---------------------------------------------------------------------------
def exercise_05():
    """Use 'Mr' or 'Ms' based on the gender field stored alongside each name."""

    print("\n--- Exercise 05: Gender-aware greetings ---")

    def greet_with_gender(people: tuple) -> None:
        """Each element is (name, gender). 'm' → 'Mr', anything else → 'Ms'."""
        for name, gender in people:
            title = "Mr" if gender.lower() == "m" else "Ms"
            print(f"Dear {title} {name}")

    # Tuple of (name, gender) pairs
    people = (
        ("Carlos", "m"),
        ("Laura",  "f"),
        ("Xoán",   "m"),
        ("Sofía",  "f"),
        ("Pedro",  "m"),
    )

    print(f"People: {people}\n")
    greet_with_gender(people)


# ---------------------------------------------------------------------------
# 06. Integer list analysis: primes, sum, average, factorials
# ---------------------------------------------------------------------------
def exercise_06():
    """Given a list of integers, find primes, compute sum/average, and list factorials."""

    print("\n--- Exercise 06: Integer list analysis ---")

    def is_prime(n: int) -> bool:
        """Returns True if n is prime. Checks divisors up to √n."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factorial(n: int) -> int:
        """Iterative factorial. factorial(0) = 1 by definition."""
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    raw_input = input("Enter integers separated by commas: ")
    try:
        numbers = [int(x.strip()) for x in raw_input.split(",")]
    except ValueError:
        print("ERROR: Integers only.")
        return

    primes     = [n for n in numbers if is_prime(n)]
    total      = sum(numbers)
    average    = total / len(numbers)
    factorials = [(n, factorial(abs(n))) for n in numbers]

    print(f"\nPrimes     : {primes}")
    print(f"Sum        : {total}")
    print(f"Average    : {average:.2f}")
    print(f"Factorials : {factorials}")


# ---------------------------------------------------------------------------
# 07. Filter list against k
# ---------------------------------------------------------------------------
def exercise_07():
    """Given a list and k, group numbers into less-than / greater-than / equal-to / multiples."""

    print("\n--- Exercise 07: Filter against k ---")

    raw_input = input("Enter integers separated by commas: ")
    try:
        numbers = [int(x.strip()) for x in raw_input.split(",")]
        k       = int(input("Enter k: "))
    except ValueError:
        print("ERROR: Integers only.")
        return

    less_than    = [n for n in numbers if n < k]
    greater_than = [n for n in numbers if n > k]
    equal_to     = [n for n in numbers if n == k]
    multiples    = [n for n in numbers if k != 0 and n % k == 0]

    print(f"\nLess than {k}    : {less_than}")
    print(f"Greater than {k} : {greater_than}")
    print(f"Equal to {k}     : {equal_to}")
    print(f"Multiples of {k} : {multiples}")


# ---------------------------------------------------------------------------
# 08. Format name tuples
# ---------------------------------------------------------------------------
def exercise_08():
    """Convert (Surname, FirstName, Initial) tuples to 'FirstName I. Surname' strings."""

    print("\n--- Exercise 08: Format name tuples ---")

    def format_names(people: list) -> list:
        """Destructuring in the comprehension makes the mapping explicit."""
        return [f"{first} {initial}. {surname}" for surname, first, initial in people]

    people = [
        ("García",    "María",   "L"),
        ("Fernández", "Carlos",  "A"),
        ("Rodríguez", "Sofía",   "M"),
        ("López",     "Pedro",   "J"),
    ]

    print("Original  (Surname, First, Initial):")
    for person in people:
        print(f"  {person}")

    print("\nFormatted (First I. Surname):")
    for name in format_names(people):
        print(f"  {name}")


# ---------------------------------------------------------------------------
# 09. Run-Length Encoding (pack)
# ---------------------------------------------------------------------------
def exercise_09():
    """Compress a list by grouping consecutive identical values with their count."""

    print("\n--- Exercise 09: Run-Length Encoding ---")

    def pack(lst: list) -> list:
        """
        RLE: consecutive equal elements are replaced by (value, count) tuples.
        Example: [1,1,2,3,3,3] → [(1,2), (2,1), (3,3)]
        """
        if not lst:
            return []

        result        = []
        current_value = lst[0]
        count         = 1

        # Compare each element to the previous; start a new group on change
        for element in lst[1:]:
            if element == current_value:
                count += 1
            else:
                result.append((current_value, count))
                current_value = element
                count         = 1

        result.append((current_value, count))  # Don't forget the last group
        return result

    raw_input = input("Enter integers separated by commas: ")
    try:
        numbers = [int(x.strip()) for x in raw_input.split(",")]
    except ValueError:
        print("ERROR: Integers only.")
        return

    print(f"\nOriginal : {numbers}")
    print(f"Packed   : {pack(numbers)}")


# ---------------------------------------------------------------------------
# 10. Matrix addition and multiplication
# ---------------------------------------------------------------------------
def exercise_10():
    """Add and multiply two 2×2 matrices."""

    print("\n--- Exercise 10: Matrix operations ---")

    def add_matrices(a: list, b: list) -> list:
        """Element-wise addition: result[i][j] = a[i][j] + b[i][j]"""
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

    def multiply_matrices(a: list, b: list) -> list:
        """
        Matrix product: result[i][j] = Σ a[i][k] × b[k][j]
        Requires: columns of A == rows of B
        """
        rows_a = len(a)
        cols_b = len(b[0])
        cols_a = len(a[0])
        return [
            [sum(a[i][k] * b[k][j] for k in range(cols_a)) for j in range(cols_b)]
            for i in range(rows_a)
        ]

    def print_matrix(matrix: list, label: str) -> None:
        print(f"\n{label}")
        for row in matrix:
            print(f"  {row}")

    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]

    print_matrix(matrix_a,                             "Matrix A:")
    print_matrix(matrix_b,                             "Matrix B:")
    print_matrix(add_matrices(matrix_a, matrix_b),     "A + B:")
    print_matrix(multiply_matrices(matrix_a, matrix_b),"A × B:")


# ---------------------------------------------------------------------------
# 11. Word wrap
# ---------------------------------------------------------------------------
def exercise_11():
    """Break a text into lines of at most n characters without splitting words."""

    print("\n--- Exercise 11: Word wrap ---")

    def word_wrap(text: str, max_length: int) -> list:
        """
        Greedy word-wrap: tries to fit as many words as possible per line.
        Words are never broken mid-word.
        """
        words   = text.split()
        lines   = []
        current = ""

        for word in words:
            candidate = (current + " " + word).strip() if current else word
            if len(candidate) <= max_length:
                current = candidate     # Word fits → extend current line
            else:
                if current:
                    lines.append(current)   # Flush current line
                current = word              # Start new line with this word

        if current:
            lines.append(current)  # Flush the last line

        return lines

    text = input("Enter text: ")
    try:
        max_len = int(input("Max line length: "))
    except ValueError:
        print("ERROR: Please enter an integer.")
        return

    print("\nWrapped output:")
    for i, line in enumerate(word_wrap(text, max_len), 1):
        print(f"  {i:>2}: '{line}'  ({len(line)} chars)")


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

MENU_OPTIONS = {
    "1" : ("Is tuple sorted ascending?",           exercise_01),
    "2" : ("Do domino tiles match?",               exercise_02),
    "3" : ("Formal greetings",                     exercise_03),
    "4" : ("Greetings from position p, n items",   exercise_04),
    "5" : ("Gender-aware greetings",               exercise_05),
    "6" : ("Integer list analysis",                exercise_06),
    "7" : ("Filter against k",                     exercise_07),
    "8" : ("Format name tuples",                   exercise_08),
    "9" : ("Run-Length Encoding",                  exercise_09),
    "10": ("Matrix operations",                    exercise_10),
    "11": ("Word wrap",                            exercise_11),
    "0" : ("Exit", make_exit("Bulletin 08 — Tuples & Lists (Advanced)")),
}


def bulletin_menu_08() -> None:
    """Entry point for Bulletin 08. Delegates menu logic to run_menu (utils/menu.py)."""
    run_menu("Bulletin 08 — Tuples & Lists (Advanced)", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_08()


# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("8", "Bulletin 08 — Tuples and Lists (Advanced)", bulletin_menu_08)