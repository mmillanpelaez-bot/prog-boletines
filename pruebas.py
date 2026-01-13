print("\n--- Ejercicio 2 ---")
print("Conversor Fahrenheit > Celsius.")

def fahrenheit_to_celsius(f_degrees: float):
    """
    Convierte una temperatura de Fahrenheit a Celsius.
    Recibe: f_degrees (float)
    Devuelve: Temperatura en Celsius (float)
    """
    c_degrees = (f_degrees - 32) * 5 / 9
    return c_degrees

while True:
    try:
        temperatura = float(input("Ingrese la temperatura Fº: "))
        print(f"La temperatura es de {fahrenheit_to_celsius(temperatura):.2f} Cº")
        break

    except ValueError:
        print("\nERROR: Introduzca una temperatura valida\n")