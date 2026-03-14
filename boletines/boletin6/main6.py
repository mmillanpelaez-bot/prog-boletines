# Boletín 6. Listas e tuplas
import math


def ejercicio1():
    """
    1. Escribir un programa que almacene as asignaturas dun curso (por exemplo Matemáticas, Física, Química, Historia e Língua) nunha lista, pregunte o usuario a nota que sacou en cada asignatura, e despois as mostre por pantalla co mensaxe En <asignatura> sacaches <nota> onde <asignatura> é cada unha das asignaturas da lista e <nota> cada unha das correspondentes notas introducidas polo usuario.
    """
    print("\n--- Ejercicio 1 ---")
    print("\nAlmacenar y mostrar")

    asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Língua']
    notas = []

    for asignatura in asignaturas:
        nota = input(f"\nIntroduce a nota que sacaches en {asignatura}: ")
        notas.append(nota)

    for i in range(len(asignaturas)):
        print(f"\nEn {asignaturas[i]} sacaches {notas[i]}")


def ejercicio2():
    """
    2. Escribir un programa que pregunte o usuario os números gañadores da lotería primitiva, os almacene nunha lista e os muestre por pantalla, ordenados de menor a maior.
    """
    print("\n--- Ejercicio 2 ---")
    print("\nAlmacenar y mostrar lista de menor a mayor")

    NUMBER_QUANTITY = 6
    MIN_RANGE = 1
    MAX_RANGE = 49

    winner_numbers = []

    while len(winner_numbers) < NUMBER_QUANTITY:
        try:
            user_input = input('\nIntroduzca los números ganadores de la primitiva: ')
            number = int(user_input)

            if not (MIN_RANGE <= number <= MAX_RANGE):
                print(f'ERROR: El número debe estar entre {MIN_RANGE} y {MAX_RANGE}.')
                continue

            if number in winner_numbers:
                print(f'ERROR: El número {number} ya se haya en la lista.')
                continue

            winner_numbers.append(number)

        except ValueError:
            print('ERROR: Entrada no válida.')

    winner_numbers.sort()
    print(winner_numbers)


def ejercicio3():
    """
    3. Escribir un programa que almacene nunha lista os números do 1 o 10 e os mostre por pantalla en orden inverso separados por comas.
    """
    print("\n--- Ejercicio 3 ---")
    print("\nMostrar lista invertida de rango de números")

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    reverse_numbers = numbers[::-1]

    print(f'{", ".join(reverse_numbers)}')


def ejercicio4():
    """
    4. Escribir un programa que almacene as asignaturas dun curso (por exemplo Matemáticas, Física, Química, Historia e Língua) nunha lista, pregunte o usuario a nota que sacou en cada asignatura e elimine da lista as asignaturas aprobadas. O fin, o programa debe mostrar por pantalla as asignaturas que o usuario ten que repetir.
    """
    print("\n--- Ejercicio 4 ---")
    print("\nMostrar asignaturas pendientes ")

    asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Língua']
    notas = []

    for asignatura in asignaturas:
        nota = float(input(f"\nIntroduce a nota que sacaches en {asignatura}: "))
        notas.append(nota)

    for i in range(len(asignaturas) - 1, -1, -1):
        if notas[i] >= 5:
            asignaturas.pop(i)
            notas.pop(i)

    print("\n--- Resultado Final ---")
    if len(asignaturas) == 0:
        print("¡Felicidades! Lo has aprobado todo.")
    else:
        print("Tienes que repetir las siguientes asignaturas: ")
        for asignatura in asignaturas:
            print(f"- {asignatura}")


def ejercicio5():
    """
    5. Escribir un programa que almacene o abecedario nunha lista, e cree outra lista a partir dela, onde non aparezan as letras que ocupen posicións múltiplos de 3, e mostre por pantalla a lista resultante.
    """
    print("\n--- Ejercicio 5 ---")
    print("\nMostrar lista filtrada a partir del abecedario ")

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # filtered_alphabet = [char for i, char in enumerate(alphabet) if i % 3 != 0]# -> forma pythonica
    filtered_alphabet = []
    for i in range(len(alphabet)):
        if i % 3 != 0:
            filtered_alphabet.append(alphabet[i])

    print(filtered_alphabet)


def ejercicio6():
    """
    6. Escribir un programa que pida o usuario unha palabra e mostre por pantalla si é un palíndromo.
    """
    print("\n--- Ejercicio 6 ---")
    print("\nVerificar palíndromo ")

    while True:
        word = input('\nWrite a word (or press Enter to exit): ').upper()
        word_inverse = word[::-1]

        if word == '':
            print('!Hasta luego!')
            break

        if not word.isalpha():
            print('ERROR: Introduce a valid word.')
        elif word == word_inverse:
            print(f'The word "{word}" is a palindrome')
        else:
            print(f'The word "{word}" is not a palindrome')


def ejercicio7():
    """
    7. Escribir un programa que pida o usuario unha palabra e mostre por pantalla o número de veces que conten cada vogal.
    """
    print("\n--- Ejercicio 7 ---")
    print("\n Vocales repetidas")

    vowels = ('A', 'E', 'I', 'O', 'U')
    word = input('Write a word: ').upper()

    for vowel in vowels:
        count = word.count(vowel)
        print(f'The vowel {vowel} appears {count} times.')


def ejercicio8():
    """
    8. Escribir un programa que almacene nunha lista os seguintes prezos, 50, 75, 46, 22, 80, 65, 8, e mostre por pantalla o menor e o maior dos prezos.
    """
    print("\n--- Ejercicio 8 ---")
    print("\n Mostrar menor/mayor precio")

    prices = [50, 75, 46, 22, 80, 65, 8]

    print(f'The highest price is {max(prices)}, while the lowest price is {min(prices)}.')


def ejercicio9():
    """
    9. Escribir un programa que almacene os vectores (1,2,3) e (-1,0,2) en dúas listas e mostre por pantalla o seu producto escalar.
    """
    print("\n--- Ejercicio 9 ---")
    print("\n Producto escalar de dos vectores")

    vector1 = [1, 2, 3]
    vector2 = [-1, 0, 2]

    # scalar_product = 0

    # for i in range(len(vector1)):
    #     scalar_product += vector1[i] * vector2[i]

    # for v1, v2 in zip(vector1, vector2): # forma pythonica
    #     scalar_product += v1 * v2

    scalar_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))  # forma más pythonica (con List Comprehension)

    print(f'El producto escalar es: {scalar_product}')


def ejercicio10():
    """
    10. Escribir un programa que almacene as matrices a = [(1,2,3),(4,5,6)] b = [(-1,0), (0, 1), (1, 1)] nunha lista e mostre por pantalla o seu produto.
    Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila nunha tupla
    """
    print("\n--- Ejercicio 10 ---")
    print("\n Producto escalar de dos matrices")

    matrix_a = [
        (1, 2, 3),
        (4, 5, 6)
    ]

    matrix_b = [
        (-1, 0),
        (0, 1),
        (1, 1)
    ]
    # result = []

    # for i in range(len(matrix_a)):
    #     result.append([])
    #
    #     for j in range(len(matrix_b[0])):
    #         scalar_product = 0
    #
    #         for k in range(len(matrix_b)):
    #             scalar_product += matrix_a[i][k] * matrix_b[k][j]
    #
    #         result[i].append(scalar_product)

    scalar_product = [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*matrix_b)]
        for row_a in matrix_a
    ]

    # print(f'El producto escalar es: {result}')
    for row in scalar_product:
        print(row)


def ejercicio11():
    """
    11. Escribir un programa que pregunte por unha mostra de números, separados por comas, os garde nunha lista e mostre por pantalla a súa media e desviación típica.
    """
    print("\n--- Ejercicio 11 ---")
    print("\nMedia y desviación típica")

    user_input = input('Inserte los números separados por comas: ')

    # forma pythonica
    # numbers = [float(x) for x in user_input.split(",")]
    #
    # avg = statistics.mean(numbers)
    # deviation = statistics.pstdev(numbers)
    #
    # print(f"Media: {avg:.2f}")
    # print(f"Desviación típica: {deviation:.2f}")

    str_list = user_input.split(",")
    numbers = [float(x.strip()) for x in str_list]

    avg = sum(numbers) / len(numbers)

    differential_sum = 0
    for num in numbers:
        differential_sum += (num - avg) ** 2

    variance = differential_sum / len(numbers)
    deviation = math.sqrt(variance)

    print(f"\nLista procesada: {numbers}")
    print(f"Media: {avg:.2f}")
    print(f"Desviación típica: {deviation:.2f}")


def salir():
    """
    Salir del menú de una forma más visual.
    """
    print("\n👋 Saliendo del menú del Boletín 6...")
    return False


OPCIONES_MENU = {
    "1" : ("Almacenar y mostrar lista", ejercicio1),
    "2" : ("Almacenar y mostrar lista de menor a mayor", ejercicio2),
    "3" : ("Mostrar lista invertida de rango de números", ejercicio3),
    "4" : ("Mostrar asignaturas pendientes", ejercicio4),
    "5" : ("Mostrar lista filtrada a partir del abecedario", ejercicio5),
    "6" : ("Verificar palíndromo", ejercicio6),
    "7" : ("Vocales repetidas", ejercicio7),
    "8" : ("Mostrar menor/mayor precio", ejercicio8),
    "9" : ("Producto escalar", ejercicio9),
    "10": ("Producto escalar de dos matrices", ejercicio10),
    '11': ("Media y desviación típica", ejercicio11),
    "0" : ("Salir", salir)
}


def menu_boletin6():
    """
    Despliega el menú principal del boletín y gestiona la navegación.

    Utiliza un patrón Dispatcher con diccionario para seleccionar
    la función correspondiente a cada ejercicio.

    :return: None
    """
    continuar = True

    while continuar:
        print("\n--- Menú de Ejercicios Boletín 6 ---")

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
    menu_boletin6()
