# PROG-Boletines

> **Subject:** Programming — DAM1  
> **Student:** Manuel Felipe Millán Peláez  
> **Teacher:** Manuel Guimarei  

---

## Index

- [PROG-Boletines](#prog-boletines)
  - [Index](#index)
  - [Description](#description)
  - [Project structure](#project-structure)
    - [Architecture notes](#architecture-notes)
  - [Setup and usage](#setup-and-usage)
  - [Bulletin status](#bulletin-status)

---

## Description

Repository with the submitted exercise bulletins for the **Programming** subject (DAM1). All bulletins are written in Python and are accessible from an interactive main menu.

---

## Project structure

```
prog-boletines/
├── main.py                   ← Entry point + auto-discovery
├── requirements.txt
├── utils/
│   ├── __init__.py
│   └── menu.py               ← Shared menu engine (run_menu, make_exit)
└── boletines/
    ├── __init__.py            ← Central registry (auto-populated at runtime)
    │
    ├── boletin_01/ … boletin_08/   ← Single-file bulletins
    │   ├── __init__.py             (empty)
    │   └── bulletin_NN.py
    │
    ├── boletin_09/            ← OOP
    │   ├── __init__.py        ← Aggregator: exposes exercise_01–03
    │   ├── bulletin_09.py
    │   ├── libro.py           ← class Book
    │   ├── consumo.py         ← class FuelConsumption
    │   └── car_account.py     ← classes Car, BankAccount
    │
    ├── boletin_10/            ← Exceptions
    │   ├── __init__.py        ← Aggregator: exposes exercise_01–02
    │   ├── bulletin_10.py
    │   ├── exceptions.py      ← InvalidDniError, InvalidLicenceError, InvalidDateError
    │   ├── person_athlete.py  ← classes Person, Athlete
    │   └── date.py            ← class Date
    │
    └── boletin_11/            ← File I/O
        ├── __init__.py        ← Aggregator: exposes exercise_01–06
        ├── bulletin_11.py
        ├── notes.py           ← Personal note manager
        ├── word_frequency.py  ← Word frequency counter
        ├── task_manager.py    ← class Task + task manager
        ├── customer_manager.py← class Customer + customer manager
        ├── inventory.py       ← CSV inventory manager
        └── contact_book.py    ← JSON contact book
```

### Architecture notes

**Auto-discovery** — `main.py` scans `boletines/` at startup using `pkgutil`, imports each `bulletin_NN.py`, and each module self-registers via `boletines.register()`. Adding a new bulletin only requires creating its folder and file; nothing else needs to change.

**Aggregator pattern** — multi-file bulletins (09–11) use `__init__.py` as the single public interface. `bulletin_NN.py` imports from the package, not from individual files directly.

**Shared menu engine** — `utils/menu.py` provides `run_menu()` and `make_exit()`, used by all bulletins.

---

## Setup and usage

Clone the repository:

```bash
git clone https://github.com/mmillanpelaez-bot/prog-boletines.git
cd prog-boletines
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the main menu:

```bash
python main.py
```

Run a specific bulletin directly:

```bash
python boletines/boletin_05/bulletin_05.py
```

> Requires **Python 3.10+**. The only external dependency is `requests` (used in bulletin 02 for the live exchange rate).

---

## Bulletin status

| #  | Topic                    | Exercises | Status         |
|----|--------------------------|-----------|----------------|
| 1  | Expressions & booleans   | 5 / 5     | ✅ Complete    |
| 2  | Algorithmics             | 5 / 5     | ✅ Complete    |
| 3  | Conditionals             | 5 / 5     | ✅ Complete    |
| 4  | Advanced conditionals    | 4 / 4     | ✅ Complete    |
| 5  | Loops                    | 13 / 13   | ✅ Complete    |
| 6  | Lists and tuples         | 11 / 11   | ✅ Complete    |
| 7  | Strings                  | 23 / 23   | ✅ Complete    |
| 8  | Tuples and lists (adv.)  | 11 / 11   | ✅ Complete    |
| 9  | Object-oriented Python   | 3 / 3     | ✅ Complete    |
| 10 | Exceptions               | 2 / 2     | ✅ Complete    |
| 11 | File I/O                 | 6 / 6     | ✅ Complete    |

**Legend:** ✅ Complete &nbsp;|&nbsp; 🔄 In progress &nbsp;|&nbsp; 📋 Pending