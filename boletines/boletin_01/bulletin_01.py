"""Bulletin 01 exercises: Expressions, operators and algebraic sequences"""

import boletines
from utils.menu import run_menu, make_exit


# ---------------------------------------------------------------------------
# 01. Results of arithmetic expressions
# ---------------------------------------------------------------------------
def exercise_01():
    """Evaluate and print the result of each arithmetic expression."""

    print("\n--- Exercise 01: Arithmetic expression results ---")

    # Each expression follows standard operator precedence (PEMDAS)
    print(f'a = {((3 + 2) % 2 - 15) / 2 * 5}')             # Result: -35.0
    print(f'b = {(6 + 6 / 7) + 35 / 2 - 8 * 5 / 4 * 2}')   # Result: 4.357...
    print(f'c = {3 + 6 * 14 % 3}')                          # Result: 3
    print(f'd = {8 + 7 * 3 + 4 * 6 / 2 % 4}')               # Result: 29.0
    print(f'e = {27 % 4 + 15 / 4}')                         # Result: 6.75
    print(f'f = {37 / 42 - 2}')                             # Result: -1.119...
    print(f'g = {9 * 2 / 3 * 25 * 3}')                      # Result: 450.0
    print(f'h = {(7 * 3 - 4 * 4) * 2 / 4 * 2}')             # Result: 5.0


# ---------------------------------------------------------------------------
# 02. Invalid variable names
# ---------------------------------------------------------------------------
def exercise_02():
    """Identify invalid variable names from the given lists."""

    print("\n--- Exercise 02: Invalid variable names ---")

    # Python identifiers cannot start with a digit, contain operators or spaces,
    # or be enclosed in quotes (that would make them strings, not names)
    print("Invalid in (a): Salto- mortal, salto + mortal, 2salto, \"salto\"")
    print("Invalid in (b): cantidade total  (spaces are not allowed)")


# ---------------------------------------------------------------------------
# 03. Algebraic expressions using arithmetic operators
# ---------------------------------------------------------------------------
def exercise_03():
    """Express algebraic formulas using Python arithmetic operators."""

    print("\n--- Exercise 03: Algebraic expressions ---")

    print('a) (m + n) / n')
    print('b) ((m + n) / p) / ((p - r) / s)')
    print('c) (m + 4) / (p - q)')
    print('d) (c * r * t / 100)')
    print('e) (m + n) / (p + (q / r))')
    print('f) (m / n) * (p + q)')
    print('g) (n * (1 + i) ** t) / ((1 + i) ** t - 1)')


# ---------------------------------------------------------------------------
# 04. Evaluate boolean expressions
# ---------------------------------------------------------------------------
def exercise_04():
    """Evaluate boolean expressions step by step and show the result."""

    print("\n--- Exercise 04: Boolean expression evaluation ---")

    # a) (True and True) → True; True == False → False
    print(f"a) True and True == False  →  {True and True == False}")

    # b) not False → True; True == True → True
    print(f"b) not False == True  →  {not False == True}")

    # c) (True and True) → True; (False == True) → False; True or False → True
    print(f"c) (True and True) or False == True  →  {(True and True) or False == True}")

    # d) (False or False) → False; (False != True) → True; False and True → False
    print(f"d) (False or False) and False != True  →  {(False or False) and False != True}")

    # e) not(True and False) → not False → True; True == False → False
    print(f"e) (not(True and False)) == False  →  {(not(True and False)) == False}")

    # f) "12" + "12" is string concatenation → "1212", not 24
    print(f'f) "12" + "12" == "24"  →  {"12" + "12" == "24"}')

    # g) "34" + "43" → "3443" == "3443" → True
    print(f'g) "34" + "43" == "3443"  →  {"34" + "43" == "3443"}')

    # h) Integer addition: 12 + 12 = 24 == 24 → True
    print(f"h) 12 + 12 == 24  →  {12 + 12 == 24}")

    # i) 34 + 43 = 77; comparing int to str is always False in Python
    print(f'i) 34 + 43 == "3443"  →  {34 + 43 == "3443"}')


# ---------------------------------------------------------------------------
# 05. Evaluate expressions with predefined variables
# ---------------------------------------------------------------------------
def exercise_05():
    """Evaluate expressions using the given variable values."""

    print("\n--- Exercise 05: Expressions with variables ---")

    # a) i=1,j=0,k=1 → (1+1)<=(0-3) and (1>=2) → False and False → False
    i, j, k = 1, 0, 1
    print(f"a) {i + k <= j - k * 3 and k >= 2}")

    # b) i=3,j=2,k=-1 → 'and' binds tighter: True or (True and False) → True
    i, j, k = 3, 2, -1
    print(f"b) {i == 3 or j <= 2 and k > 0}")

    # c) tipo=10, rede=7.5 → 10 < 9.0 → False
    tipo, rede = 10, 7.5
    print(f"c) {tipo < rede + 1.5}")

    # d) 1993 % 400 = 393 ≠ 0 → False
    ano = 1993
    print(f"d) {ano % 400 == 0}")

    # e) False or (5 > 2) → True
    print(f"e) {3 == 2 or 5 > 1 + 1}")

    # f) 3 > 4 → False; short-circuit: False and ... → False
    print(f"f) {5 - 2 > 4 and not(0.5 == 1 / 5)}")

    # g) a=2,b=5,c=6,d=10 → False or (False and True) → False
    a, b, c, d = 2, 5, 6, 10
    print(f"g) {a >= b or a >= c and a < d}")

    # h) (7<6) and (8<10) or (4<7) → False and True or True → True
    print(f"h) {a + b < c and a + c < d or 2 * a < a + b}")

    # i) not(10<10) and not(10<6) or 11<=10 → True and True or False → True
    print(f"i) {not(a * b < d) and not(a * b < c) or b + c <= d}")


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

MENU_OPTIONS = {
    "1": ("Arithmetic expression results",  exercise_01),
    "2": ("Invalid variable names",         exercise_02),
    "3": ("Algebraic expressions",          exercise_03),
    "4": ("Boolean expression evaluation",  exercise_04),
    "5": ("Expressions with variables",     exercise_05),
    "0": ("Exit", make_exit("Bulletin 01 — Expressions & Booleans")),
}


def bulletin_menu_01() -> None:
    """Entry point for Bulletin 01. Delegates all menu logic to run_menu."""
    run_menu("Bulletin 01 — Expressions & Booleans", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_01()


# ---------------------------------------------------------------------------
# Self-registration
# ---------------------------------------------------------------------------
boletines.register("1", "Bulletin 01 — Expressions & Booleans", bulletin_menu_01)