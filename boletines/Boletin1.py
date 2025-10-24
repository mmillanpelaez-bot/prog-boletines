print('\nBoletín 1.')

# 1.
def boletin1_1():

    print("\n--- Ejercicio 1: Resultado de las expresiones ---")
    
    print(f'a = {((3 + 2) % 2 - 15) / 2 * 5}') # Resultado: -35.0
    print(f'b = {(6 + 6 / 7) + 35 / 2 -8 * 5 / 4 * 2}') # Resultado: 4.357142857142858
    print(f'c = {3 + 6 * 14 % 3}') # Resultado: 3
    print(f'd = {8 + 7 * 3 + 4 * 6 /2 % 4}') # Resultado: 29.0
    print(f'e = {27 % 4 +15 / 4}') # Resultado: 6.75
    print(f'f = {37 / 42 - 2}') # Resultado: -1.119047619047619
    print(f'g = {9 * 2 / 3 * 25 * 3}') # Resultado: 450.0
    print(f'h = {(7 * 3 - 4 * 4) * 2 / 4 * 2}') # Resultado: 5.0

# 2.
def boletin1_2():

    print("\n--- Ejercicio 2 ---")
    print('Variables non válidos:')

    print('Invalidos en (a): Salto- mortal, salto + mortal, 2salto, "salto"')
    print("Invalidos en (b): cantidade total")

# 3.
def boletin1_3():

    print("\n--- Ejercicio 3 ---")
    print('Expresar, utilizando operadores aritméticos:')

    print('a) (m + n) / n')
    print('b) ((m + n) / p) / ((p - r) / s)')
    print('c) (m + 4) / (p - q)')
    print('d) (c * r * t / 100)')
    print('e) (m + n) / (p + (q / r))')
    print('f) (m / n) * (p + q)')
    print('g) (n * (1 + i) ** t) / ((1 + i) ** t - 1)')

# 4.
def boletin1_4():

    print("\n--- Exercicio 4 ---")
    print('Avalia as seguintes expresións:')

    # a) True and True == False
    # (True and True) es True
    # True == False es False
    print(f"a) True and True == False -> {True and True == False}") # Resultado: False

    # b) not False == True
    # (not False) es True
    # True == True es True
    print(f"b) not False == True -> {not False == True}") # Resultado: True

    # c) (True and True) or False == True
    # (True and True) es True
    # (False == True) es False
    # True or False es True
    print(f"c) (True and True) or False == True -> {(True and True) or False == True}") # Resultado: True

    # d) (False or False) and False != True
    # (False or False) es False
    # (False != True) es True
    # False and True es False
    print(f"d) (False or False) and False != True -> {(False or False) and False != True}") # Resultado: False

    # e) (not(True and False)) == False
    # (True and False) es False
    # not(False) es True
    # True == False es False
    print(f"e) (not(True and False)) == False -> {(not(True and False)) == False}") # Resultado: False

    # f) “12” + “12” == “24”
    # "12" + "12" es "1212" (concatenación de cordas)
    # "1212" == "24" es False
    print(f'f) "12" + "12" == "24" -> {"12" + "12" == "24"}') # Resultado: False

    # g) “34” + “43” == “3443”
    # "34" + "43" es "3443"
    # "3443" == "3443" es True
    print(f'g) "34" + "43" == "3443" -> {"34" + "43" == "3443"}') # Resultado: True

    # h) 12 + 12 == 24
    # 12 + 12 es 24 (suma aritmestica)
    # 24 == 24 es True
    print(f"h) 12 + 12 == 24 -> {12 + 12 == 24}") # Resultado: True

    # i) 34 + 43 == “3443”
    # 34 + 43 es 77
    # 77 == "3443" es False (comparación de enteiro con corda)
    print(f'i) 34 + 43 == “3443” -> {34 + 43 == "3443"}') # Resultado: False

# 5.
def boletin1_5():
    
    print("\n--- Ejercicio 5 ---")
    print('Avaliar espresións, tendo en conta as variables')

    # a) i = 1, j = 0, k = 1
    # i + k <= j – k * 3 and k >= 2
    # (1 + 1) <= (0 - 1 * 3) and (1 >= 2)
    # 2 <= (0 - 3) and False
    # 2 <= -3 and False
    # False and False
    i=1; j=0; k=1
    print(f"a) {i + k <= j - k * 3 and k >= 2}") # Resultado: False

    # b) i = 3, j = 2, k = -1
    # i == 3 or j <= 2 and k > 0
    # (3 == 3) or (2 <= 2) and (-1 > 0)
    # True or True and False
    # True or (True and False)  <- 'and' tiene prioridad
    # True or False
    i=3; j=2; k=-1
    print(f"b) {i == 3 or j <= 2 and k > 0}") # Resultado: True

    # c) tipo = 10, rede = 7.5
    # tipo < rede + 1.5
    # 10 < (7.5 + 1.5)
    # 10 < 9.0
    tipo=10; rede=7.5
    print(f"c) {tipo < rede + 1.5}") # Resultado: False

    # d) ano = 1993
    # ano % 400 == 0
    # 1993 % 400 es 393
    # 393 == 0
    ano=1993
    print(f"d) {ano % 400 == 0}") # Resultado: False

    # e) 3 == 2 or 5 > 1 + 1
    # (3 == 2) or (5 > 2)
    # False or True
    print(f"e) {3 == 2 or 5 > 1 + 1}") # Resultado: True

    # f) 5 – 2 > 4 and not(0.5 == 1 / 5)
    # (5 - 2) > 4 and not(0.5 == 0.2)
    # 3 > 4 and not(False)
    # False and True
    print(f"f) {5 - 2 > 4 and not(0.5 == 1 / 5)}") # Resultado: False

    # g) a = 2, b = 5, c = 6, d = 10
    # a >= b or a >= c and a < d
    # (2 >= 5) or (2 >= 6) and (2 < 10)
    # False or False and True
    # False or (False and True)
    # False or False
    a=2; b=5; c=6; d=10
    print(f"g) {a >= b or a >= c and a < d}") # Resultado: False

    # h) a = 2, b = 5, c = 6, d = 10
    # a + b < c and a + c < d or 2 * a < a + b
    # ((2 + 5) < 6) and ((2 + 6) < 10) or ((2 * 2) < (2 + 5))
    # (7 < 6) and (8 < 10) or (4 < 7)
    # False and True or True
    # (False and True) or True
    # False or True
    a=2; b=5; c=6; d=10
    print(f"h) {a + b < c and a + c < d or 2 * a < a + b}") # Resultado: True

    # i) a = 2, b = 5, c = 6, d = 10
    # !(a * b < d) and !(a * b < c) or b + c <= d
    # Asumiendo que '!' es el operador 'not'
    # not(a * b < d) and not(a * b < c) or (b + c <= d)
    # not(2 * 5 < 10) and not(2 * 5 < 6) or (5 + 6 <= 10)
    # not(10 < 10) and not(10 < 6) or (11 <= 10)
    # not(False) and not(False) or False
    # True and True or False
    # (True and True) or False
    # True or False
    a=2; b=5; c=6; d=10
    print(f"i) {not(a * b < d) and not(a * b < c) or b + c <= d}") # Resultado: True


def menu_boletin1():

    while True:
        
        print("\n--- Menú de Ejercicios Boletín 1 ---")
        print("1. Resultado de las expresiones")
        print("2. Variables no válidos")
        print("3. Expresar con operadores aritméticos")
        print("4. Evaluar expresiones lógicas")
        print("5. Evaluar expresiones con variables")
        print("6. Salir")

        choice = input("Seleccione un ejercicio (1-6): ")

        if choice == '1':
            boletin1_1()
        elif choice == '2':
            boletin1_2()
        elif choice == '3':
            boletin1_3()
        elif choice == '4':
            boletin1_4()
        elif choice == '5':
            boletin1_5()
        elif choice == '6': # break option
            print("\nSaliendo del menú de Boletín 1.")
            break
        else:  # else print error
            print("Opción no válida. Inténtelo de nuevo.")

# if __name__ == "__main__": #for testing purposes
    menu_boletin1()
