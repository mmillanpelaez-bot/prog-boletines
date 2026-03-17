"""Exercise 01 — class Book"""


class Book:
    def __init__(self, title: str, author: str, year: int, pages: int, rating: float):
        self._title  = title
        self._author = author
        self._year   = year
        self._pages  = pages
        self.rating  = rating  # Uses property setter for validation

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Title cannot be empty.")
        self._title = value.strip()

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Author cannot be empty.")
        self._author = value.strip()

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        if not (1000 <= value <= 9999):
            raise ValueError("Year must be a 4-digit number.")
        self._year = value

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if value < 1:
            raise ValueError("Page count must be at least 1.")
        self._pages = value

    @property
    def rating(self) -> float:
        return self._rating

    @rating.setter
    def rating(self, value: float) -> None:
        if not (0.0 <= value <= 10.0):
            raise ValueError("Rating must be between 0 and 10.")
        self._rating = value

    def display(self) -> None:
        print(f"\n  Title  : {self._title}")
        print(f"  Author : {self._author}")
        print(f"  Year   : {self._year}")
        print(f"  Pages  : {self._pages}")
        print(f"  Rating : {self._rating:.1f} / 10")

    def __str__(self) -> str:
        return f'"{self._title}" by {self._author} ({self._year})'
