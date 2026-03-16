"""Bulletin 07 exercises: Strings"""

import boletines
from utils.menu import run_menu, make_exit


# ---------------------------------------------------------------------------
# 01. String length
# ---------------------------------------------------------------------------
def exercise_01():
    """Show the length of the string 'Isto é Python!'"""
    print(len("Isto é Python!"))


# ---------------------------------------------------------------------------
# 02. Character by character
# ---------------------------------------------------------------------------
def exercise_02():
    """Print each character of 'Python' on its own line."""
    for character in "Python":
        print(character)


# ---------------------------------------------------------------------------
# 03. Reverse a string
# ---------------------------------------------------------------------------
def exercise_03():
    """Reverse 'Python para todos' using slice notation."""
    print("Python para todos"[::-1])


# ---------------------------------------------------------------------------
# 04. Remove spaces
# ---------------------------------------------------------------------------
def exercise_04():
    """Remove all spaces from 'Guido Van Rossum creou Python'."""
    print("Guido Van Rossum creou Python".replace(" ", ""))


# ---------------------------------------------------------------------------
# 05. Count vowels and consonants
# ---------------------------------------------------------------------------
def exercise_05():
    """Count vowels and consonants in 'Python Python Python', ignoring spaces."""

    vowels     = []
    consonants = []
    text       = "Python Python Python".lower().replace(" ", "")

    for letter in text:
        if letter.isalpha():
            if letter in "aeiou":
                vowels.append(letter)
            else:
                consonants.append(letter)

    print(f"Vowels     ({len(vowels)}): {vowels}")
    print(f"Consonants ({len(consonants)}): {consonants}")


# ---------------------------------------------------------------------------
# 06. Split and re-join a string
# ---------------------------------------------------------------------------
def exercise_06():
    """Split 'www.phytonparatodos.com' into two parts and concatenate them back."""

    text   = "www. phytonparatodos. com"
    part_1 = text[0:11]
    part_2 = text[11:]

    print(f"Part 1 : {part_1}")
    print(f"Part 2 : {part_2}")
    print(f"Joined : {part_1 + part_2}")


# ---------------------------------------------------------------------------
# 07. Upper and lower case conversion
# ---------------------------------------------------------------------------
def exercise_07():
    """Convert 'Phytoneros' to uppercase, store it, then convert to lowercase."""

    upper_case = "Phytoneros".upper()
    lower_case = "Phytoneros".lower()

    print(f"Upper: {upper_case}")
    print(f"Lower: {lower_case}")


# ---------------------------------------------------------------------------
# 08. String equality
# ---------------------------------------------------------------------------
def exercise_08():
    """Compare 'Python' and 'JavaScript' for equality."""

    if "Python" == "JavaScript":
        print("They are equal.")
    else:
        print("They are not equal.")


# ---------------------------------------------------------------------------
# 09. Vowel substitution
# ---------------------------------------------------------------------------
def exercise_09():
    """Replace all 'e' with 'a' in 'Jeve jeve jeve' → 'java java java'."""
    print("Jeve jeve jeve".replace("e", "a"))


# ---------------------------------------------------------------------------
# 10. Character type counter
# ---------------------------------------------------------------------------
def exercise_10():
    """Count letters, digits and whitespace in a given string."""

    def count_characters(text: str) -> None:
        letters = 0
        digits  = 0
        spaces  = 0

        for char in text:
            if char.isalpha():
                letters += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1

        print(f"Letters   : {letters}")
        print(f"Digits    : {digits}")
        print(f"Whitespace: {spaces}")

    sample = "Ola, son alumno de DAM1, e son programador desde o 2025"
    print(f"Text: '{sample}'\n")
    count_characters(sample)


# ---------------------------------------------------------------------------
# 11. Slice operations on a string
# ---------------------------------------------------------------------------
def exercise_11():
    """
    Given a string, print:
    a) first two characters
    b) last three characters
    c) every other character
    d) string + its reverse
    """

    def first_two(s: str) -> str:
        return s[:2]

    def last_three(s: str) -> str:
        return s[-3:]

    def every_other(s: str) -> str:
        return s[::2]

    def forward_and_backward(s: str) -> str:
        return s + s[::-1]

    sample = "Galicia"
    print(f"String          : {sample}")
    print(f"First two       : {first_two(sample)}")
    print(f"Last three      : {last_three(sample)}")
    print(f"Every other     : {every_other(sample)}")
    print(f"Forward+backward: {forward_and_backward(sample)}")


# ---------------------------------------------------------------------------
# 12. String/character operations
# ---------------------------------------------------------------------------
def exercise_12():
    """
    Given a string and a character:
    a) Replace all spaces with the character
    b) Insert the character between each letter
    c) Replace all digits with the character
    d) Insert the character every 3 digits
    """

    def replace_spaces(text: str, char: str) -> str:
        return text.replace(" ", char)

    def insert_between(text: str, separator: str) -> str:
        return separator.join(text)

    def replace_digits(text: str, char: str) -> str:
        return "".join(char if c.isdigit() else c for c in text)

    def insert_every_three_digits(text: str, separator: str) -> str:
        digits_only = "".join(c for c in text if c.isdigit())
        parts       = [digits_only[i:i + 3] for i in range(0, len(digits_only), 3)]
        return separator.join(parts)

    print(replace_spaces("meu arquivo de texto.txt", "_"))
    print(insert_between("separar", ","))
    print(replace_digits("sua clave e: 1540", "X"))
    print(insert_every_three_digits("2552552550", "."))


# ---------------------------------------------------------------------------
# 13. Limited replacements/insertions
# ---------------------------------------------------------------------------
def exercise_13():
    """
    Versions of exercise_12 functions that accept a maximum replacement count.

    Python's str.replace(old, new, count) natively supports a limit for
    simple substitutions. For character-level filtering (digits), we loop
    and track a counter manually.
    """

    print("\n--- Exercise 13: Limited replacements ---")

    def replace_spaces_limited(text: str, char: str, max_n: int) -> str:
        """Replace at most max_n spaces with char."""
        return text.replace(" ", char, max_n)

    def insert_between_limited(text: str, separator: str, max_n: int) -> str:
        """Insert separator between characters, but only max_n times."""
        if max_n <= 0:
            return text
        result = text[0]
        insertions = 0
        for c in text[1:]:
            if insertions < max_n:
                result += separator
                insertions += 1
            result += c
        return result

    def replace_digits_limited(text: str, char: str, max_n: int) -> str:
        """Replace at most max_n digit characters with char."""
        result  = []
        count   = 0
        for c in text:
            if c.isdigit() and count < max_n:
                result.append(char)
                count += 1
            else:
                result.append(c)
        return "".join(result)

    text = input("  Text: ").strip()
    char = input("  Replacement character: ").strip()

    while True:
        try:
            max_n = int(input("  Max replacements: "))
            if max_n >= 0:
                break
            print("  Please enter a non-negative integer.")
        except ValueError:
            print("  ERROR: Invalid value.")

    print(f"\n  a) Space replacement (max {max_n})  : {replace_spaces_limited(text, char, max_n)}")
    print(f"  b) Insert between    (max {max_n})  : {insert_between_limited(text, char, max_n)}")
    print(f"  c) Digit replacement (max {max_n})  : {replace_digits_limited(text, char, max_n)}")


# ---------------------------------------------------------------------------
# 14. Thousands separator
# ---------------------------------------------------------------------------
def exercise_14():
    """Format a long integer with dot thousands separators. E.g. 1234567890 → 1.234.567.890"""

    def format_with_thousands(number: int) -> str:
        return f"{number:,}".replace(",", ".")

    print(format_with_thousands(1234567890))


# ---------------------------------------------------------------------------
# 15. First letters, title case and words starting with A
# ---------------------------------------------------------------------------
def exercise_15():
    """
    Given a string:
    i)   Return the acronym (first letter of each word, uppercase)
    ii)  Return the string in title case
    iii) Return only the words starting with 'A'
    """

    def process_string(text: str) -> tuple:
        words      = text.split()
        acronym    = "".join(word[0].upper() for word in words)
        title_case = text.title()
        a_words    = " ".join(word for word in words if word.lower().startswith("a"))
        return acronym, title_case, a_words

    sample = "Antes de abrir la republica arxentina con un universal serial bus"
    acronym, title, a_words = process_string(sample)

    print(f"Original  : '{sample}'")
    print(f"i)  Acronym  : {acronym}")
    print(f"ii) Title    : {title}")
    print(f"iii) A-words : {a_words}")


# ---------------------------------------------------------------------------
# 16. Consonants, vowels, vowel shift
# ---------------------------------------------------------------------------
def exercise_16():
    """
    a) Return only consonants from the input string
    b) Return only vowels
    c) Replace each vowel with the next one in the cycle (a→e, e→i, i→o, o→u, u→a)
    """

    print("\n--- Exercise 16: Consonants, vowels and vowel shift ---")

    VOWELS      = set("aeiouAEIOU")
    VOWEL_CYCLE = {"a": "e", "e": "i", "i": "o", "o": "u", "u": "a",
                   "A": "E", "E": "I", "I": "O", "O": "U", "U": "A"}

    text = input("  Enter text: ")

    consonants   = "".join(c for c in text if c.isalpha() and c not in VOWELS)
    only_vowels  = "".join(c for c in text if c in VOWELS)
    shifted      = "".join(VOWEL_CYCLE.get(c, c) for c in text)

    print(f"\n  Original   : {text}")
    print(f"  Consonants : {consonants}")
    print(f"  Vowels     : {only_vowels}")
    print(f"  Shifted    : {shifted}")


# ---------------------------------------------------------------------------
# 17. Phrase palindrome
# ---------------------------------------------------------------------------
def exercise_17():
    """Check if a sentence is a palindrome, ignoring spaces and case."""

    def is_palindrome(text: str) -> bool:
        cleaned = "".join(c for c in text if c.isalnum()).lower()
        return cleaned == cleaned[::-1]

    sample = "anita lava la tina"
    print(f"'{sample}' is palindrome: {is_palindrome(sample)}")


# ---------------------------------------------------------------------------
# 18. Substring and alphabetical order
# ---------------------------------------------------------------------------
def exercise_18():
    """
    a) Check if the second string is a substring of the first
    b) Return which of two strings comes first alphabetically
    """

    print("\n--- Exercise 18: Substring and alphabetical order ---")

    s1 = input("  First string : ")
    s2 = input("  Second string: ")

    # a) Substring check — case-sensitive by default
    if s2 in s1:
        print(f'\n  a) "{s2}" IS a substring of "{s1}"')
    else:
        print(f'\n  a) "{s2}" is NOT a substring of "{s1}"')

    # b) Alphabetical order — case-insensitive comparison
    key1, key2 = s1.lower(), s2.lower()
    if key1 < key2:
        print(f'  b) "{s1}" comes first alphabetically.')
    elif key1 > key2:
        print(f'  b) "{s2}" comes first alphabetically.')
    else:
        print(f'  b) Both strings are equivalent alphabetically.')


# ---------------------------------------------------------------------------
# 19. Binary to decimal
# ---------------------------------------------------------------------------
def exercise_19():
    """
    Convert a binary string (ones and zeros only) to its decimal value.

    Two approaches shown side by side:
      - Built-in : int(binary, 2)          → concise, idiomatic
      - Manual   : positional sum          → shows the underlying maths
    """

    print("\n--- Exercise 19: Binary to decimal ---")

    while True:
        binary = input("  Enter binary string (e.g. 1011): ").strip()
        if binary and all(c in "01" for c in binary):
            break
        print("  ERROR: Only '0' and '1' characters are allowed.")

    # Built-in conversion
    decimal_builtin = int(binary, 2)

    # Manual positional sum: each bit × 2^position (right to left = position 0)
    decimal_manual = sum(int(bit) * (2 ** i) for i, bit in enumerate(reversed(binary)))

    print(f"\n  Binary        : {binary}")
    print(f"  Decimal       : {decimal_builtin}")
    print(f"  Manual check  : {decimal_manual}")

    # Show the expanded form for clarity
    terms = " + ".join(
        f"{bit}×2^{i}" for i, bit in enumerate(reversed(binary)) if bit == "1"
    )
    print(f"  Expanded      : {terms} = {decimal_builtin}")


# ---------------------------------------------------------------------------
# 20. Masking functions
# ---------------------------------------------------------------------------
def exercise_20():
    """
    Given a text and a character:
    i)  Return a new string of the same length filled entirely with that character
    ii) Return a string where positions NOT matching the character are replaced with '-'
    """

    print("\n--- Exercise 20: Masking functions ---")

    text = input("  Text            : ")
    char = input("  Mask character  : ")

    if len(char) != 1:
        print("  ERROR: Please enter exactly one character.")
        return

    # i) Full mask — every position becomes the mask character
    full_mask = char * len(text)

    # ii) Partial mask — keep matching positions, replace others with '-'
    partial_mask = "".join(c if c == char else "-" for c in text)

    print(f"\n  Original     : {text}")
    print(f"  i)  Full mask   : {full_mask}")
    print(f"  ii) Partial mask: {partial_mask}")


# ---------------------------------------------------------------------------
# 21. Password validator
# ---------------------------------------------------------------------------
def exercise_21():
    """
    Validate a password against four rules:
      - At least 8 characters
      - At least one uppercase letter
      - At least one lowercase letter
      - At least one digit

    Returns True only when all rules are met.
    """

    print("\n--- Exercise 21: Password validator ---")

    def validate_password(password: str) -> tuple[bool, list[str]]:
        """
        Returns (is_valid, list_of_failed_rules).
        An empty error list means the password is valid.
        """
        errors = []

        if len(password) < 8:
            errors.append("At least 8 characters required.")
        if not any(c.isupper() for c in password):
            errors.append("At least one uppercase letter required.")
        if not any(c.islower() for c in password):
            errors.append("At least one lowercase letter required.")
        if not any(c.isdigit() for c in password):
            errors.append("At least one digit required.")

        return len(errors) == 0, errors

    while True:
        password = input("  Password: ")
        if password:
            break
        print("  Password cannot be empty.")

    valid, errors = validate_password(password)

    if valid:
        print("  ✅ Valid password.")
    else:
        print("  ❌ Invalid password:")
        for error in errors:
            print(f"     - {error}")

    return valid  # Exposed so other functions can call this as a utility


# ---------------------------------------------------------------------------
# 22. Name formatter
# ---------------------------------------------------------------------------
def exercise_22():
    """
    Clean and capitalise a name + surname:
      - Strip leading/trailing whitespace
      - Collapse internal multiple spaces
      - Capitalise the first letter of each word
    """

    print("\n--- Exercise 22: Name formatter ---")

    raw = input("  Enter name and surname: ")

    # split() with no argument splits on any whitespace and removes empty tokens,
    # so it handles multiple spaces and leading/trailing spaces in one step
    parts     = raw.split()
    formatted = " ".join(part.capitalize() for part in parts)

    print(f"  Raw       : '{raw}'")
    print(f"  Formatted : '{formatted}'")


# ---------------------------------------------------------------------------
# 23. Simple text analyser
# ---------------------------------------------------------------------------
def exercise_23():
    """
    Analyse a text and report:
      - Word count
      - Character count (excluding spaces)
      - The longest word (and its length)
    """

    print("\n--- Exercise 23: Simple text analyser ---")

    text = input("  Enter text: ")

    if not text.strip():
        print("  No text to analyse.")
        return

    words      = text.split()
    char_count = len(text.replace(" ", ""))
    longest    = max(words, key=len)

    print(f"\n  Words          : {len(words)}")
    print(f"  Characters     : {char_count}  (spaces excluded)")
    print(f"  Longest word   : '{longest}'  ({len(longest)} chars)")


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

MENU_OPTIONS = {
    "1" : ("String length",                        exercise_01),
    "2" : ("Character by character",               exercise_02),
    "3" : ("Reverse a string",                     exercise_03),
    "4" : ("Remove spaces",                        exercise_04),
    "5" : ("Count vowels and consonants",          exercise_05),
    "6" : ("Split and re-join a string",           exercise_06),
    "7" : ("Upper and lower case",                 exercise_07),
    "8" : ("String equality",                      exercise_08),
    "9" : ("Vowel substitution",                   exercise_09),
    "10": ("Character type counter",               exercise_10),
    "11": ("Slice operations",                     exercise_11),
    "12": ("String/character operations",          exercise_12),
    "13": ("Limited replacements",                 exercise_13),
    "14": ("Thousands separator",                  exercise_14),
    "15": ("Acronym, title case, A-words",         exercise_15),
    "16": ("Consonants, vowels, shift",            exercise_16),
    "17": ("Phrase palindrome",                    exercise_17),
    "18": ("Substring and alphabetical",           exercise_18),
    "19": ("Binary to decimal",                    exercise_19),
    "20": ("Masking functions",                    exercise_20),
    "21": ("Password validator",                   exercise_21),
    "22": ("Name formatter",                       exercise_22),
    "23": ("Simple text analyser",                 exercise_23),
    "0" : ("Exit", make_exit("Bulletin 07 — Strings")),
}


def bulletin_menu_07():
    """Entry point for Bulletin 07. Delegates menu logic to run_menu (utils/menu.py)."""
    run_menu("Bulletin 07 — Strings", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_07()


# ---------------------------------------------------------------------------
# Self-registration
# ---------------------------------------------------------------------------
boletines.register("7", "Bulletin 07 — Strings", bulletin_menu_07)