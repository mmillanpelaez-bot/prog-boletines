"""Menú de ejercicios del Boletín 5: Bucles y estructuras iterativas"""

# 1. Escribir un ciclo definido para imprimir por pantalla tódolos números entre	10 e 20.
def ejercicio1():
    print("\n--- Ejercicio 1 ---")
    print("Imprimir un rango de numeros.")

    for number in range(10,21):
        print(number)

# 2. Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius. Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.
def ejercicio2():
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

# 3. Utiliza o programa anterior para xerar unha táboa de conversión de temperaturas, dende 0º F ata 120º F, de 10 en 10.
def ejercicio3():
    print("\n--- Ejercicio 3 ---")
    print("Tabla conversion temperatura.")
    #
    # for celsius in range(0, 121, 10):
    #     print (fahrenheit, celsius)
    #
    # #= (5/9)*(celsius - 32)
    #

# 4. Escribir un programa que imprima tódolos números pares entre dous números que se lle pidan o usuario.
def ejercicio4():
    print("\n--- Ejercicio 4 ---")
    print("Numeros pares.")

# 5. Escribir un programa que reciba un número n por parámetro e imprima os primeiros n números triangulares, xunto co seu índice. Os números triangulares obteñense mediante a suma dos números naturales dende 1 ata n. É dicir, si se piden os primeros 5 números triangulares, o programa debe imprimir:
#   1 - 1
#   2 - 3
#   3 - 6
#   4 - 10
#   5 - 15
#   Nota: facelo usando e sen usar a ecuación n ∗ (n + 1) / 2. Cal realiza máis operacións?
def ejercicio5():
    print("\n--- Ejercicio 5 ---")
    print("Primer numero triangular")


# 6. Escribir un programa que tome unha cantidade m de valores ingresados polo usuario, a cada un lle calcule o factorial e imprima o resultado xunto co número de orden correspondiente.
def ejercicio6():
    print("\n--- Ejercicio 6 ---")
    print("Calcular factorial")
# 7. Escribir un programa que imprima por pantalla tódalas fichas de dominó, de unha por liña e sen repetir.
def ejercicio7():
    print("Fichas domino.")
    def domino ():
        for n in range(7):
            for m in range(n, 7):
                print("La ficha es:", n, '|', m)
    domino()
# 8. Modificar o programa anterior para que poida xerar fichas dun xogo que pode ter números de 0 a n.
def ejercicio8():
    print("Reutilizar fichas.")
    def generador_fichas(n):
        for i in range(n+1):
            for j in range(i, n+1):
                print("La ficha es:", i, '|', j)

    try:
        m = int(input("Escribe el número máximo de la ficha: "))
        generador_fichas(m)
    except ValueError:
        print("Error: Por favor escribe un número entero.")
# 9. Calcula a cantidade de números negativos, positivos e ceros que hai nun grupo de 10 números enteiros.
def ejercicio9():
    print("Calcular numeros negativos")

# 10. Deseña un programa que calcule o área dun rectángulo cuxa base e altura pides por teclado. Asegúrate que estes valores sexan positivos, para eso valida os datos.
def ejercicio10():
    print("Calcular area rectangulo")

# 11. Codifica un programa que solicite un número e visualice a táboa de multiplicar dese número. O programa seguirá pedindo números ata que o usuario pulse o número cero.
def ejercicio11():
    print("Tabla de multiplicar de n")

# 12. Codifica un programa que lea o soldo de cada un dos traballadores dunha empresa e obteña o número deles que ganan entre 1000 e 1750 €, ámbolos dous incluídos e, a porcentaxe de traballadores que ganan menos de 1000 €. Tendo en conta que non se coñece con antelación o numero de traballadores da empresa e non se admiten os soldos negativos (utiliza como condición de fin un soldo 0).
def ejercicio12():
    print("Rango sueldo trabajadores")

# 13. Solicita o usuario un número n e debuxa un triángulo de base e altura n. Si o usuario teclea o número 4 o triángulo sería da seguinte forma:
#       *
#      * *
#     * * *
#    * * * *
def ejercicio13():
    print("Dibujo triangulo base n")


def salir():
    """
    Salir del menú de una forma más visual.
    """
    print("\n👋 Saliendo del menú del Boletín 5...")
    return False

OPCIONES_MENU = {
    "1":  ("Imprimir rango de números", ejercicio1),
    "2":  ("Conversor Fahrenheit > Celsius", ejercicio2),
    "3":  ("Tabla conversion temperatura", ejercicio3),
    "4":  ("Numeros pares", ejercicio4),
    "5":  ("Primer numero triangular", ejercicio5),
    "6":  ("Calcular factorial", ejercicio6),
    "7":  ("Fichas domino.", ejercicio7),
    "8":  ("Reutilizar fichas", ejercicio8),
    "9":  ("Calcular numeros negativos", ejercicio9),
    "10": ("Calcular area rectangulo", ejercicio10),
    "11": ("Tabla de multiplicar de n", ejercicio11),
    "12": ("Rango sueldo trabajadores", ejercicio12),
    "13": ("Dibujo triangulo base n", ejercicio13),
    "0":  ("Salir", salir)
}

def menu_boletin5():
    """
    Despliega el menú principal del boletín y gestiona la navegación.

    Utiliza un patrón Dispatcher con diccionario para seleccionar
    la función correspondiente a cada ejercicio.

    :return: None
    """
    continuar = True
    
    while continuar:
        print("\n--- Menú de Ejercicios Boletín 5 ---")
        
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
    menu_boletin5()