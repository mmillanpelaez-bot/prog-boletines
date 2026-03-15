"""
boletines/__init__.py
─────────────────────
Bulletin registry.

Each bulletin module calls register() once at import time to add itself
to the REGISTRY dict. main.py then reads REGISTRY to build its menu —
no manual import list anywhere.

Adding a new bulletin:
  1. Create boletines/boletinN/bulletin_NN.py
  2. Call register() at the bottom of that file
  3. Done — main.py picks it up automatically

The registry maps the display key (str) to a (label, menu_function) tuple,
the same shape as every MENU_OPTIONS dict in the project.
"""

# Global registry populated by each bulletin module at import time
REGISTRY: dict[str, tuple[str, callable]] = {}


def register(key: str, label: str, menu_fn: callable) -> None:
    """
    Register a bulletin so main.py can discover it automatically.

    Parameters
    ----------
    key     : str       Menu key shown to the user, e.g. "05"
    label   : str       Human-readable description, e.g. "Bulletin 05 — Loops"
    menu_fn : callable  The bulletin_menu_NN function to call
    """
    REGISTRY[key] = (label, menu_fn)