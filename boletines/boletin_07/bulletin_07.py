"""Bulletin 07 exercises: Strings"""

import boletines
from utils.menu import run_menu


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
    part_1 = text[0:11]   # 'www. phyton'
    part_2 = text[11:]    # 'paratodos. com'

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
        """Counts letters, digits and whitespace characters in text."""
        letters   = 0
        digits    = 0
        spaces    = 0

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
        return s[::2]  # Step 2 skips every second character

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
        """a) 'meu arquivo de texto.txt' + '_' → 'meu_arquivo_de_texto.txt'"""
        return text.replace(" ", char)

    def insert_between(text: str, separator: str) -> str:
        """b) 'separar' + ',' → 's,e,p,a,r,a,r'"""
        return separator.join(text)

    def replace_digits(text: str, char: str) -> str:
        """c) 'clave: 1540' + 'X' → 'clave: XXXX'"""
        return "".join(char if c.isdigit() else c for c in text)

    def insert_every_three_digits(text: str, separator: str) -> str:
        """d) '2552552550' + '.' → '255.255.255.0'"""
        digits_only = "".join(c for c in text if c.isdigit())
        parts       = [digits_only[i:i + 3] for i in range(0, len(digits_only), 3)]
        return separator.join(parts)

    print(replace_spaces("meu arquivo de texto.txt", "_"))
    print(insert_between("separar", ","))
    print(replace_digits("sua clave e: 1540", "X"))
    print(insert_every_three_digits("2552552550", "."))


# ---------------------------------------------------------------------------
# 13. Limited replacements/insertions   [TODO]
# ---------------------------------------------------------------------------
def exercise_13():
    """Modify exercise_12 functions to accept a maximum number of replacements."""
    pass  # TODO


# ---------------------------------------------------------------------------
# 14. Thousands separator
# ---------------------------------------------------------------------------
def exercise_14():
    """Format a long integer with dot thousands separators. E.g. 1234567890 → 1.234.567.890"""

    def format_with_thousands(number: int) -> str:
        # Python's :, format uses comma; we replace it with a dot
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
        words = text.split()

        # i) Acronym: join the first (uppercased) letter of each word
        acronym    = "".join(word[0].upper() for word in words)

        # ii) Title case: built-in str.title() capitalises first letter of each word
        title_case = text.title()

        # iii) Words starting with 'A' (case-insensitive)
        a_words    = " ".join(word for word in words if word.lower().startswith("a"))

        return acronym, title_case, a_words

    sample = "Antes de abrir la republica arxentina con un universal serial bus"
    acronym, title, a_words = process_string(sample)

    print(f"Original  : '{sample}'")
    print(f"i)  Acronym  : {acronym}")
    print(f"ii) Title    : {title}")
    print(f"iii) A-words : {a_words}")


# ---------------------------------------------------------------------------
# 16. Consonants, vowels, vowel shift   [TODO]
# ---------------------------------------------------------------------------
def exercise_16():
    """
    a) Return only consonants
    b) Return only vowels
    c) Replace each vowel with the next vowel (a→e, e→i, i→o, o→u, u→a)
    """
    pass  # TODO


# ---------------------------------------------------------------------------
# 17. Phrase palindrome
# ---------------------------------------------------------------------------
def exercise_17():
    """Check if a sentence is a palindrome, ignoring spaces and case."""

    def is_palindrome(text: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase before comparing
        cleaned = "".join(c for c in text if c.isalnum()).lower()
        return cleaned == cleaned[::-1]

    sample = "anita lava la tina"
    print(f"'{sample}' is palindrome: {is_palindrome(sample)}")


# ---------------------------------------------------------------------------
# 18. Substring and alphabetical order   [TODO]
# ---------------------------------------------------------------------------
def exercise_18():
    """
    a) Check if the second string is a substring of the first
    b) Return which of two strings comes first alphabetically
    """
    pass  # TODO


# ---------------------------------------------------------------------------
# 19. Binary to decimal   [TODO]
# ---------------------------------------------------------------------------
def exercise_19():
    """Convert a binary string (ones and zeros) to its decimal value."""
    pass  # TODO


# ---------------------------------------------------------------------------
# 20. Masking functions   [TODO]
# ---------------------------------------------------------------------------
def exercise_20():
    """
    i)  Return a new string of the same length filled with a given character
    ii) Return a string with dashes and the character at positions where it matches
    """
    pass  # TODO


# ---------------------------------------------------------------------------
# 21. Password validator   [TODO]
# ---------------------------------------------------------------------------
def exercise_21():
    """
    Validate a password: at least 8 chars, one uppercase, one lowercase, one digit.
    Return a boolean.
    """
    pass  # TODO


# ---------------------------------------------------------------------------
# 22. Name formatter   [TODO]
# ---------------------------------------------------------------------------
def exercise_22():
    """Remove leading/trailing spaces and capitalise the first letter of name and surname."""
    pass  # TODO


# ---------------------------------------------------------------------------
# 23. Simple text analyser   [TODO]
# ---------------------------------------------------------------------------
def exercise_23():
    """Count words, characters and find the longest word in a text."""
    pass  # TODO


# ---------------------------------------------------------------------------
# Menu configuration
# ---------------------------------------------------------------------------

def exit_menu():
    """Signal the menu loop to stop by returning False."""
    print("\n👋 Exiting Bulletin 07...")
    return False


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
    "13": ("Limited replacements [TODO]",          exercise_13),
    "14": ("Thousands separator",                  exercise_14),
    "15": ("Acronym, title case, A-words",         exercise_15),
    "16": ("Consonants, vowels, shift [TODO]",     exercise_16),
    "17": ("Phrase palindrome",                    exercise_17),
    "18": ("Substring and alphabetical [TODO]",    exercise_18),
    "19": ("Binary to decimal [TODO]",             exercise_19),
    "20": ("Masking functions [TODO]",             exercise_20),
    "21": ("Password validator [TODO]",            exercise_21),
    "22": ("Name formatter [TODO]",                exercise_22),
    "23": ("Simple text analyser [TODO]",          exercise_23),
    "0" : ("Exit",                                 exit_menu),
}


def bulletin_menu_07():
    """Entry point for Bulletin 07. Delegates menu logic to run_menu (utils/menu.py)."""
    run_menu("Bulletin 07 — Strings", MENU_OPTIONS)


if __name__ == "__main__":
    bulletin_menu_07()


# ---------------------------------------------------------------------------
# Self-registration — fires once on import, adds this bulletin to REGISTRY
# ---------------------------------------------------------------------------
boletines.register("7", "Bulletin 07 — Strings", bulletin_menu_07)