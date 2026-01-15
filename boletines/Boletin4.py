from math import pi

print('\nBoletín 4: Condicionales')

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

    print("\n--- Ejercicio 4 ---")
    print("Números en letras.\n")

# menú
def menu_boletin4():

    while True:
        
        print("\n--- Menú de Ejercicios Boletín 4 ---")
        print("1. ")
        print("2. ")
        print("3. ")
        print("4. ")
        print("5. ")
        print("6. ")
        print("7. ")
        print("8. ")
        print("9. ")
        print("10. ")
        print("11. ")
        print("0. Salir")

        choice = input("Seleccione un ejercicio: ")

        if choice == '1':
            ejercicio1()
        elif choice == '2':
            ejercicio2()
        elif choice == '3':
            ejercicio3()
        elif choice == '4':
            ejercicio4()
        elif choice == '5':
            ejercicio5()
        elif choice == '6':
            ejercicio6()
        elif choice == '7':
            ejercicio7()
        elif choice == '8':
            ejercicio8()
        elif choice == '9':
            ejercicio9()
        elif choice == '10':
            ejercicio10()
        elif choice == '11':
            ejercicio11()
        elif choice == '0': # break option
            print("\nSaliendo del menú del Boletín 5.")
            break
        else:  # else print error
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu_boletin7()