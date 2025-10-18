print('Boletín 5.')

# 1. Escribir un ciclo definido para imprimir por pantalla tódolos números entre	10 e 20.
print("Ejercicio 1.")
for number in range(10,21):
    print(number)

# 2. Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius. Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.
print("Ejercicio 2.")
def fahrenheit_to_celsius (f_degrees):
    return (f_degrees - 32) * 5/9
#    = float(input("Escribe el valor en Fahrenheit: "))
#fahrenheit = (celsius*9/5)+32
#print(fahrenheit)

# 3. Utiliza o programa anterior para xerar unha táboa de conversión de temperaturas, dende 0º F ata 120º F, de 10 en 10.
print("Ejercicio 3.")
#for celsius in range(0, 121, 10):
    #= (5/9)*(celsius - 32)
 #   print (fahrenheit, celsius)

# 4. Escribir un programa que imprima tódolos números pares entre dous números que se lle pidan o usuario.
print("Ejercicio 4.")

# 5. Escribir un programa que reciba un número n por parámetro e imprima os primeiros n números triangulares, xunto co seu índice. Os números triangulares obteñense mediante a suma dos números naturales dende 1 ata n. É dicir, si se piden os primeros 5 números triangulares, o programa debe imprimir:
#   1 - 1
#   2 - 3
#   3 - 6
#   4 - 10
#   5 - 15
#   Nota: facelo usando e sen usar a ecuación n ∗ (n + 1) / 2. Cal realiza máis operacións?
print("Ejercicio 5.")

# 6. Escribir un programa que tome unha cantidade m de valores ingresados polo usuario, a cada un lle calcule o factorial e imprima o resultado xunto co número de orden correspondiente.
print("Ejercicio 6.")

# 7. Escribir un programa que imprima por pantalla tódalas fichas de dominó, de unha por liña e sen repetir.
print("Ejercicio 7.")
def domino ():
    for n in range(7):
        for m in range(n, 7):
            print("La ficha es:", n, '|', m)
domino()
# 8. Modificar o programa anterior para que poida xerar fichas dun xogo que pode ter números de 0 a n.
print("Ejercicio 8.")
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
print("Ejercicio 9.")

# 10. Deseña un programa que calcule o área dun rectángulo cuxa base e altura pides por teclado. Asegúrate que estes valores sexan positivos, para eso valida os datos.
print("Ejercicio 10.")

# 11. Codifica un programa que solicite un número e visualice a táboa de multiplicar dese número. O programa seguirá pedindo números ata que o usuario pulse o número cero.
print("Ejercicio 11.")

# 12. Codifica un programa que lea o soldo de cada un dos traballadores dunha empresa e obteña o número deles que ganan entre 1000 e 1750 €, ámbolos dous incluídos e, a porcentaxe de traballadores que ganan menos de 1000 €. Tendo en conta que non se coñece con antelación o numero de traballadores da empresa e non se admiten os soldos negativos (utiliza como condición de fin un soldo 0).
print("Ejercicio 12.")

# 13. Solicita o usuario un número n e debuxa un triángulo de base e altura n. Si o usuario teclea o número 4 o triángulo sería da seguinte forma:
#       *
#      * *
#     * * *
#    * * * *
print("Ejercicio 13.")

# 14. Codificar o programa que solicite 10 números por consola e calcule a súa suma. Si o usuario introduce en calquera momento o número 999, deixa de solicitar máis números e presenta o valor da súma acadada ata ese momento.
