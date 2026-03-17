"""Exercise 02 — class FuelConsumption (car dashboard)"""


class FuelConsumption:
    """
    Models the fuel consumption dashboard of a car.

    Attributes
    ----------
    km          : float  Distance driven (km)
    litres      : float  Fuel consumed (litres)
    avg_speed   : float  Average speed (km/h)
    fuel_price  : float  Fuel price per litre (€)
    """

    def __init__(self, km: float, litres: float, avg_speed: float, fuel_price: float):
        self.km         = km
        self.litres     = litres
        self.avg_speed  = avg_speed
        self.fuel_price = fuel_price

    @property
    def km(self) -> float:
        return self._km

    @km.setter
    def km(self, value: float) -> None:
        if value < 0:
            raise ValueError("Distance cannot be negative.")
        self._km = value

    @property
    def litres(self) -> float:
        return self._litres

    @litres.setter
    def litres(self, value: float) -> None:
        if value < 0:
            raise ValueError("Fuel consumed cannot be negative.")
        self._litres = value

    @property
    def avg_speed(self) -> float:
        return self._avg_speed

    @avg_speed.setter
    def avg_speed(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Average speed must be greater than 0.")
        self._avg_speed = value

    @property
    def fuel_price(self) -> float:
        return self._fuel_price

    @fuel_price.setter
    def fuel_price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Fuel price must be greater than 0.")
        self._fuel_price = value

    def get_time(self) -> float:
        """Travel time in hours: t = d / v"""
        return self._km / self._avg_speed

    def avg_consumption(self) -> float:
        """Average fuel consumption in litres per 100 km."""
        if self._km == 0:
            return 0.0
        return (self._litres / self._km) * 100

    def consumption_euros(self) -> float:
        """Total fuel cost in euros."""
        return self._litres * self._fuel_price

    def display(self) -> None:
        print(f"\n  Distance        : {self._km:.1f} km")
        print(f"  Fuel consumed   : {self._litres:.2f} L")
        print(f"  Average speed   : {self._avg_speed:.1f} km/h")
        print(f"  Fuel price      : {self._fuel_price:.3f} €/L")
        print(f"  Travel time     : {self.get_time():.2f} h")
        print(f"  Avg. consumption: {self.avg_consumption():.2f} L/100km")
        print(f"  Total fuel cost : {self.consumption_euros():.2f} €")


def fuel_consumption_main():
    print("\n--- Exercise 02: Fuel Consumption class ---")

    while True:
        try:
            km         = float(input("Distance driven (km)     : "))
            litres     = float(input("Fuel consumed (litres)   : "))
            avg_speed  = float(input("Average speed (km/h)     : "))
            fuel_price = float(input("Fuel price per litre (€) : "))
            dashboard  = FuelConsumption(km, litres, avg_speed, fuel_price)
            break
        except ValueError as e:
            print(f"  ERROR: {e}")

    dashboard.display()
