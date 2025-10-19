print('Boletín 4: Condicionales')
# 1.
print("Ejercicio 1")
#Vendas anuais			Artigo de consumo
#baixo <= 100 produtos
#>100 e < = 500			medio
#> 500 e < = 1000			alto
#> 1000 				primeira necesidade

# 2. Area calculator
def boletin4_2():

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
                from math import pi
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