"""Menú de ejercicios del Boletín 4: Funciones, módulos y excepciones"""

from math import pi


# 1. Un almacén clasifica os seus produtos segundo a seguinte táboa de
# vendas anuais:
def ejercicio1():
    print("\n--- Ejercicio 1 ---")
    print("Clasificador de productos.")

    product_name = input("Nome do producto: ")
    annual_sales = int(input("Ventas anuais: "))

    product_type = ""

    if annual_sales <= 100:
        product_type = "baixo"
    elif annual_sales <= 500:
        product_type = "medio"
    elif annual_sales <= 1000:
        product_type = "alto"
    else:
        product_type = "primeira necesidade"

    print(f"El artículo del producto '{product_name}' es de tipo: {product_type}")

# 2. Area calculator
def ejercicio2():

    print("\n--- Ejercicio 2 ---")
    print("Calculador de áreas de figuras geométricas.")

    while True:

        # print table
        print ("\n--Calculador de Areas--")
        print("1. Rectangulo")
        print("2. Triángulo")
        print("3. Círculo")
        print("4. Salir")

        # ask input
        option = input("Selecciona un número: ")

        # rectangle
        if option == "1":
            def area_rectangle():
                length_str = input("Escribe el largo del rectángulo: ")
                width_str = input("Escribe el ancho del rectángulo: ")
                lenght = float(length_str)
                width = float(width_str)
                area = lenght*width
                print("El area del rectángulo es:", area)
            area_rectangle()

        # triangle
        elif option == "2":
            def area_triangle():
                base_str = input("Escribe la base del triángulo: ")
                height_str = input("Escribe la altura del triángulo: ")
                base = float(base_str)
                height = float(height_str)
                area = base*height
                print("El area del triángulo es:", area)
            area_triangle()

        # circle
        elif option == "3":
            def area_circle():
                radius_str = input("Escribe el radio del círculo: ")
                radius = float(radius_str)
                area = pi*radius**2
                print("El area del círculo es:", area)
            area_circle()

        # break option
        elif option == "4":
            print("¡Hasta la vista!")
            break

        # else print error
        else: print("Error: Por favor elija un valor correcto.")

# 3. Utiliza o operador ternario para calcular o valor absoluto dun número
# que se solicita o usuario por teclado.
def ejercicio3():

    print("\n--- Ejercicio 3 ---")
    print("Valor absoluto (Ternario).\n")

    number = float(input("Introduce un número: "))

    absolute_value = number if number >= 0 else -number

    print(f"El valor absoluto de {number:g} es {absolute_value:g}")

# 4. Escribe un programa que solicite o usuario un número comprendido
# entre 1 e 99. O programa ten que mostralo con letras, por exemplo, para
# o 56, mostrará: “Cincuenta e seis”.
def ejercicio4():
# TODO: añadir excepciones de 'no numeros' y de rango.
    print("\n--- Ejercicio 4 ---")
    print("Números en letras.\n")

    unidad = {
        0: 'cero',
        1: 'uno',
        2: 'dos',
        3: 'tres',
        4: 'cuatro',
        5: 'cinco',
        6: 'seis',
        7: 'siete',
        8: 'ocho',
        9: 'nueve',
    }
    decena = {
        1: 'diez',
        2: 'veinte',
        3: 'treinta',
        4: 'cuarenta',
        5: 'cincuenta',
        6: 'sesenta',
        7: 'setenta',
        8: 'ochenta',
        9: 'noventa'
    }
    especiales = {
        11: 'once',
        12: 'doce',
        13: 'trece',
        14: 'catorce',
        15: 'quince',
        16: 'dieciséis',
        17: 'diecisiete',
        18: 'dieciocho',
        19: 'diecinueve',
        21: 'veintiuno',
        22: 'veintidós',
        23: 'veintitrés',
        24: 'veinticuatro',
        25: 'veinticinco',
        26: 'veintiséis',
        27: 'veintisiete',
        28: 'veintiocho',
        29: 'veintinueve'
    }

    while True:
        entrada = input('Escriba el número (o pulse Enter para salir): ')

        if  entrada == '':
            print('!Hasta luego!')
            break

        numero = int(entrada)

        extraer_decena = numero // 10
        extraer_unidad = numero % 10

        if numero in especiales:
            print(f'{especiales[numero]}')
        elif numero in range(0,10):
            print(unidad[extraer_unidad])
        elif extraer_unidad == 0:
            print(decena[extraer_decena])
        else:
            print(f'{decena[extraer_decena]} y {unidad[extraer_unidad]}')


def salir():
    """
    Salir del menú de una forma más visual.
    """
    print("\n👋 Saliendo del menú del Boletín 4...")
    return False

OPCIONES_MENU = {
    "1":  ("Clasificador de productos", ejercicio1),
    "2":  ("Calculador de áreas", ejercicio2),
    "3":  ("Valor absoluto (Ternario)", ejercicio3),
    "4":  ("Números en letras", ejercicio4),
    "0":  ("Salir", salir)
}

def menu_boletin4():
    """
    Despliega el menú principal del boletín y gestiona la navegación.

    Utiliza un patrón Dispatcher con diccionario para seleccionar
    la función correspondiente a cada ejercicio.

    :return: None
    """
    continuar = True
    
    while continuar:
        print("\n--- Menú de Ejercicios Boletín 4 ---")
        
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
    menu_boletin4()