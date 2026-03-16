"""Exercise 03 — Task manager with binary file persistence"""

import os
import pickle

TASKS_FILE = "tasks.dat"


class Task:
    """
    Represents a scheduled task.

    Attributes
    ----------
    date        : str   Date (DD/MM/YYYY)
    time        : str   Time (HH:MM)
    duration    : int   Duration in minutes
    name        : str   Short task name
    description : str   Longer description
    status      : str   "pending" | "in_progress" | "done"
    """

    VALID_STATUSES = ("pending", "in_progress", "done")

    def __init__(self, date: str, time: str, duration: int,
                 name: str, description: str, status: str = "pending"):
        self.date        = date
        self.time        = time
        self.duration    = duration
        self.name        = name
        self.description = description
        self.status      = status

    def display(self, index: int = None) -> None:
        prefix = f"[{index}] " if index is not None else ""
        print(f"\n  {prefix}{self.name} ({self.status})")
        print(f"    Date     : {self.date} at {self.time}")
        print(f"    Duration : {self.duration} min")
        print(f"    Desc.    : {self.description}")

    def __str__(self) -> str:
        return f"Task('{self.name}', {self.date} {self.time}, {self.status})"


def _load_tasks() -> list[Task]:
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "rb") as f:
        return pickle.load(f)


def _save_tasks(tasks: list[Task]) -> None:
    with open(TASKS_FILE, "wb") as f:
        pickle.dump(tasks, f)
    print(f"  Tasks saved to '{TASKS_FILE}'.")


def _input_task() -> Task:
    date     = input("  Date (DD/MM/YYYY): ").strip()
    time     = input("  Time (HH:MM)     : ").strip()
    duration = int(input("  Duration (min)   : "))
    name     = input("  Name             : ").strip()
    desc     = input("  Description      : ").strip()
    return Task(date, time, duration, name, desc)


def task_manager():
    print("\n--- Exercise 03: Task manager ---")
    tasks = _load_tasks()
    print(f"  Loaded {len(tasks)} task(s).")

    while True:
        print("\n  1. Add task")
        print("  2. List tasks")
        print("  3. Update task status")
        print("  4. Delete task")
        print("  5. Save and exit")
        choice = input("  >> ").strip()

        if choice == "1":
            try:
                tasks.append(_input_task())
                print("  Task added.")
            except ValueError as e:
                print(f"  ERROR: {e}")

        elif choice == "2":
            if not tasks:
                print("  No tasks.")
            else:
                for i, task in enumerate(tasks, 1):
                    task.display(i)

        elif choice == "3":
            if not tasks:
                print("  No tasks to update.")
                continue
            for i, task in enumerate(tasks, 1):
                print(f"  {i}. {task}")
            try:
                idx    = int(input("  Task number: ")) - 1
                print(f"  Statuses: {Task.VALID_STATUSES}")
                status = input("  New status: ").strip()
                if status not in Task.VALID_STATUSES:
                    print("  Invalid status.")
                else:
                    tasks[idx].status = status
                    print("  Updated.")
            except (ValueError, IndexError):
                print("  Invalid selection.")

        elif choice == "4":
            if not tasks:
                print("  No tasks to delete.")
                continue
            for i, task in enumerate(tasks, 1):
                print(f"  {i}. {task}")
            try:
                idx     = int(input("  Delete task number: ")) - 1
                removed = tasks.pop(idx)
                print(f"  Deleted: {removed.name}")
            except (ValueError, IndexError):
                print("  Invalid selection.")

        elif choice == "5":
            _save_tasks(tasks)
            break
        else:
            print("  Invalid option.")
