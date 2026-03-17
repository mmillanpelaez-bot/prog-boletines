"""Exercise 01 — classes Person and Athlete with custom exceptions"""

import re
from boletines.boletin_10.exceptions import InvalidDniError, InvalidLicenceError

VALID_SPORT_CODES = {"fut", "bal", "bas", "ten", "nat", "atl", "vol", "box", "cic", "rwb"}


class Person:
    """A person with a validated DNI (Spanish national ID)."""

    _DNI_LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"

    def __init__(self, name: str, dni: str):
        self._name = name
        self.dni   = dni

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()

    @property
    def dni(self) -> str:
        return self._dni

    @dni.setter
    def dni(self, value: str) -> None:
        """
        Validates DNI format and check digit.
        Format: 8 digits + 1 uppercase letter.
        Check digit: LETTERS[int(digits) % 23]
        """
        if not re.match(r"^\d{8}[A-Z]$", value):
            raise InvalidDniError(value)
        if value[-1] != self._DNI_LETTERS[int(value[:8]) % 23]:
            raise InvalidDniError(value)
        self._dni = value

    def display(self) -> None:
        print(f"\n  Name : {self._name}")
        print(f"  DNI  : {self._dni}")

    def __str__(self) -> str:
        return f"Person(name='{self._name}', dni='{self._dni}')"


class Athlete(Person):
    """A person who also holds a sports federation licence."""

    def __init__(self, name: str, dni: str, licence: str):
        super().__init__(name, dni)
        self.licence = licence

    @property
    def licence(self) -> str:
        return self._licence

    @licence.setter
    def licence(self, value: str) -> None:
        """
        Licence format: aaaadddnnnnnn
          aaaa   — 4-digit year
          ddd    — sport code (3 lowercase letters)
          nnnnnn — 6-digit unique number
        Example: 2024fut000123
        """
        if not re.match(r"^\d{4}[a-z]{3}\d{6}$", value):
            raise InvalidLicenceError(value)
        if value[4:7] not in VALID_SPORT_CODES:
            raise InvalidLicenceError(value)
        self._licence = value

    def display(self) -> None:
        super().display()
        print(f"  Licence: {self._licence}")

    def __str__(self) -> str:
        return f"Athlete(name='{self._name}', dni='{self._dni}', licence='{self._licence}')"
