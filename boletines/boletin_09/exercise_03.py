"""Exercise 03 — classes Car and BankAccount"""


class Car:
    """Models a car with a speed that can be accelerated and braked."""

    def __init__(self):
        self._speed = 0

    def get_speed(self) -> int:
        return self._speed

    def accelerate(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Acceleration amount must be positive.")
        self._speed += amount
        print(f"  Accelerating +{amount} km/h → current speed: {self._speed} km/h")

    def brake(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Braking amount must be positive.")
        self._speed = max(0, self._speed - amount)
        print(f"  Braking -{amount} km/h → current speed: {self._speed} km/h")

    def __str__(self) -> str:
        return f"Car(speed={self._speed} km/h)"


class BankAccount:
    """Models a bank account with deposit, withdrawal and transfer operations."""

    def __init__(self, holder: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._holder  = holder
        self._balance = balance

    @property
    def holder(self) -> str:
        return self._holder

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        print(f"  [{self._holder}] Deposited {amount:.2f}€ → balance: {self._balance:.2f}€")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds. Available: {self._balance:.2f}€")
        self._balance -= amount
        print(f"  [{self._holder}] Withdrew {amount:.2f}€ → balance: {self._balance:.2f}€")

    def transfer(self, destination: "BankAccount", amount: float) -> None:
        self.withdraw(amount)
        destination.deposit(amount)

    def __str__(self) -> str:
        return f"BankAccount(holder='{self._holder}', balance={self._balance:.2f}€)"
