"""Exercise 02 — class Date with full validation"""

from boletines.boletin_10.exceptions import InvalidDateError

_DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def _is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def _max_day(month: int, year: int) -> int:
    if month == 2 and _is_leap_year(year):
        return 29
    return _DAYS_IN_MONTH[month]


class Date:
    """
    A validated calendar date.

    Constraints
    -----------
    year  : 1970 – 2999
    month : 1 – 12
    day   : 1 – 28/29/30/31 (depends on month and leap year)
    """

    MIN_YEAR = 1970
    MAX_YEAR = 2999

    def __init__(self, day: int, month: int, year: int):
        self._year  = self._validate_year(year)
        self._month = self._validate_month(month)
        self._day   = self._validate_day(day, month, year)

    @staticmethod
    def _validate_year(year: int) -> int:
        if not (Date.MIN_YEAR <= year <= Date.MAX_YEAR):
            raise InvalidDateError(
                f"Year {year} out of range. Allowed: {Date.MIN_YEAR}–{Date.MAX_YEAR}."
            )
        return year

    @staticmethod
    def _validate_month(month: int) -> int:
        if not (1 <= month <= 12):
            raise InvalidDateError(f"Month {month} out of range. Allowed: 1–12.")
        return month

    @staticmethod
    def _validate_day(day: int, month: int, year: int) -> int:
        max_d = _max_day(month, year)
        if not (1 <= day <= max_d):
            raise InvalidDateError(
                f"Day {day} invalid for {month}/{year}. Allowed: 1–{max_d}."
            )
        return day

    @property
    def day(self) -> int:
        return self._day

    @day.setter
    def day(self, value: int) -> None:
        self._day = self._validate_day(value, self._month, self._year)

    @property
    def month(self) -> int:
        return self._month

    @month.setter
    def month(self, value: int) -> None:
        self._month = self._validate_month(value)
        self._day   = self._validate_day(self._day, value, self._year)

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        self._year = self._validate_year(value)
        self._day  = self._validate_day(self._day, self._month, value)

    def display(self) -> None:
        leap = " (leap year)" if _is_leap_year(self._year) else ""
        print(f"\n  Date  : {self}")
        print(f"  Year  : {self._year}{leap}")
        print(f"  Month : {self._month}")
        print(f"  Day   : {self._day} (max this month: {_max_day(self._month, self._year)})")

    def __str__(self) -> str:
        return f"{self._day:02d}/{self._month:02d}/{self._year}"

    def __repr__(self) -> str:
        return f"Date(day={self._day}, month={self._month}, year={self._year})"
