"""Custom exceptions for Bulletin 10."""


class InvalidDniError(ValueError):
    """Raised when a DNI does not match the expected format (8 digits + 1 letter)."""

    def __init__(self, dni: str):
        super().__init__(
            f"Invalid DNI '{dni}'. Expected format: 8 digits followed by 1 uppercase letter "
            f"(e.g. 12345678Z). The letter must also be the correct check digit."
        )


class InvalidLicenceError(ValueError):
    """Raised when a sports licence does not match format: aaaadddnnnnnn."""

    def __init__(self, licence: str):
        super().__init__(
            f"Invalid licence '{licence}'. Expected format: 4-digit year + "
            f"sport code (3 letters, e.g. fut/bal/bas) + 6-digit number (e.g. 2024fut000123)."
        )


class InvalidDateError(ValueError):
    """Raised when a date value is out of the allowed range."""

    def __init__(self, message: str):
        super().__init__(message)
