print('\nBoletín 3: Condicionales')

# 1. Confirmador de números naturales
def ejercicio1():
    while True:
        try:
            entrada = float(input("\nEscriba un número: "))

            if entrada >= 0:
                print(f"{entrada} es un número positivo.")
            else:
                print(f"{entrada} no es un número positivo.")
            break

        except ValueError:
            print("ERROR: Eso no es un número.")

# 2- Escribe un programa no que se tecleen dous números. Se o
# primeiro é maior ou igual que o segundo,visualizaremos a
# resta. En calquera caso visualizaremos a suma.
def ejercicio2():
    while True:
        try:
            num1 = float(input("\nEscriba el primer número: "))
            num2 = float(input("Escriba el segundo número: "))

            if num1 >= num2:
                print(f"La resta de {num1} y {num2} es: {num1 - num2}")

            print(f"La suma de {num1} y {num2} es: {num1 + num2}")
            break

        except ValueError:
            print("ERROR: Eso no es un número.")

# 3- Codificar o programa que o teclear un número por teclado,
# mostre por consola o signo “ + “ se o número é positivo, o signo
# “ –“ se é negativo e “ 0 “ se é cero.
def ejercicio3():
    while True:

        try:
            numero = float(input("\nEscriba un número: "))

            if numero > 0:
                print("+")
            elif numero == 0:
                print("0")
            elif numero < 0:
                print("-")
            break

        except ValueError:
            print("ERROR: Eso no es un número.")

# 4- Coñecidos, o nome e o peso de dúas persoas, o programa
# escribirá por consola os datos da persoa que pesa máis e a
# diferenza de peso entre elas.
def ejercicio4():
    nome1 = input("¿Cómo se llama la primera persona? ")
    nome2 = input("¿Cómo se llama la segunda persona? ")

    peso1 = float(input(f"¿Cuánto pesa {nome1}? "))
    peso2 = float(input(f"¿Cuánto pesa {nome2}? "))

    if peso1 > peso2:
        print(f"{nome1} pesa {peso1 - peso2} kg más que {nome2}.")
    elif peso2 > peso1:
        print(f"{nome2} pesa {peso2 - peso1} kg más que {nome1}.")
    else:
        print(f"{nome1} y {nome2} pesan lo mismo, {peso1} kg.")

# 5- Dados 3 números que se supoñen distintos, indicar cal é o
# maior.
def ejercicio5():

    num1 = float(input("Escribe el primer número: "))
    num2 = float(input("Escribe el segundo número: "))
    num3 = float(input("Escribe el tercer número: "))

    # if num1 > num2:
    #     if num1 > num3:
    #         print(f"{num1} es el número más grande.")
    # elif num2 > num1:
    #     if num2 > num3:
    #         print(f"{num2} es el número más grande.")
    # elif num3 > num1:
    #     if num3 > num2:
    #         print(f"{num3} es el número más grande.")

    mayor = max(num1, num2, num3)
    print(f"{mayor} es el número más grande.")

def menu_boletin3():
    while True:

        print("\n--- Menú de Ejercicios del Boletín 2 ---")
        print("1. Confirmador de números naturales")
        print("2. Booleano con opeacion aritmetica")
        print("3. Signo matematico equivalente al numero")
        print("4. Comparar peso de dos personas")
        print("5. Comparar numero mayor")
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
        elif choice == '0':  # break option
            print("\nSaliendo del menú del Boletín 3.")
            break
        else:  # else print error
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu_boletin3()