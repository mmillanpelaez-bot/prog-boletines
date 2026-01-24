import requests

# 1. Algoritmo que calcula el área de un triángulo.
def ejercicio1():

    print("\n--- Ejercicio 1 ---")
    print("Cálculo do área dun triángulo.")

    base = 4
    height = 3
    area = base*height/2
    print(f'El area del triángulo es:{area}')

# 2. Algoritmo que calcula el área de un cuadrado.
def ejercicio2():

    print("\n--- Ejercicio 2 ---")
    print("Cálculo del área de un cuadrado.")

    side = 3
    area = side**2
    print(f'El area del cuadrado es: {area}')

# 3. Algoritmo que cambia euros a dólares.
def ejercicio3():

    print("\n--- Ejercicio 3 ---")
    print("Cambio de euros a dólares.")

    def get_exchange_rate():
        try:
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

# 4. Secuencia algebráica
"""
1. INICIO
2. PEDIR 'Introduce el primer numero: 
3. LEER num1
4. PEDIR 'Introduce el segundo numero: 
5. LEER num2
6. CALCULAR suma = num1 + num2
7. MOSTRAR 'suma = ',{suma}
8. CALCULAR resta = num1 - num2
9. MOSTRAR 'resta = '{resta} 
10. CALCULAR producto = num1 * num2
11. MOSTRAR 'producto = '{producto}
    IF num2 != 0:
12. CALCULAR cociente = num1 / num2
13. MOSTRAR 'cociente = '{cociente}
    ELSE:
    MOSTRAR 'No se puede dividir entre 0'
14. FIN
"""
def ejercicio4():

    num1 = float(input('Escribe el primer número: '))
    num2 = float(input('Escribe el segundo número: '))

    print(f'suma = {num1 + num2}')
    print(f'resta = {num1 - num2}')
    print(f'producto = {num1 * num2}')
    if num2 != 0:
        print(f'cociente = {num1 / num2}')
    else:
        print('cociente = Error: No se puede dividir entre 0')

# 5. milla náutica a metro
def ejercicio5():
    mllmar = float(input("Distancia en millas marinas: "))
    mtr = mllmar * 1852
    print(f"Distancia en metros: {mtr}")


def salir():
    print("\n👋 Saliendo del menú del Boletín 2...")
    return False

OPCIONES_MENU = {
    "1":  ("Calculador del área de un triángulo", ejercicio1),
    "2":  ("Cálculo del área de un cuadrado", ejercicio2),
    "3":  ("Cambio de euros a dólares", ejercicio3),
    "4":  ("Secuencia algebráica", ejercicio4),
    "5":  ("Milla náutica a metro", ejercicio5),
    "0":  ("Salir", salir)
}

def menu_boletin2():
    continuar = True
    
    while continuar:
        print("\n--- Menú de Ejercicios Boletín 2 ---")
        
        for clave, valor in OPCIONES_MENU.items():
            descripcion = valor[0]
            print(f"{clave}. {descripcion}")

        choice = input("\n>> Seleccione un ejercicio: ")

        if choice in OPCIONES_MENU:
            accion = OPCIONES_MENU[choice][1]
            
            try:
                resultado = accion() 
                
                if resultado is False:
                    continuar = False
                else:
                    input("\n[Intro para continuar...]")
                    
            except NameError:
                print(f"⚠️  Error: La función {accion.__name__} no está definida todavía.")
            except Exception as e:
                print(f"⚠️  Ocurrió un error inesperado en el ejercicio: {e}")
                
        else:
            print("❌ Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu_boletin2()