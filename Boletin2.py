print('Boletín 2: Algorítmia')

# Menú selector de ejercicio
from functions import exercise_menu
exercise_menu()

# 1. Algoritmo que calcula o área dun triángulo.
base = 4
height = 3
area = base*height
print("El area del triángulo es:", area)

# 2.

# 3. Algoritmo que cambia euros a dólares.
def eur_to_usd():

    def get_exchange_rate():
        try:
            import requests
            # Try to fetch the live rate from Frankfurter API
            url = "https://api.frankfurter.dev/v1/latest?from=EUR&to=USD"
            response = requests.get(url, timeout=5)  # timeout in seconds
            response.raise_for_status()  # raise error if status != 200
            data = response.json()
            return data["rates"]["USD"]
        except Exception as e:
            print("⚠️ Could not fetch live exchange rate.")
            print(f"Reason: {e}")
            # Fallback: ask user to input manually
            return float(input("Please enter the exchange rate (USD per EUR): "))

    # Main program
    exchange_rate = get_exchange_rate()
    print(f"Using EUR → USD rate: {exchange_rate}")

    euros = float(input("Introduce euros: "))
    dolares = euros * exchange_rate

    print(f"{euros} € = {dolares:.2f} $ (rate: {exchange_rate:.4f})")

eur_to_usd()
