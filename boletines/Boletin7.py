print('\nBoletín 7. Cadeas de caracteres')
#
# 1. Mostra a lonxitude do texto: “ Isto é Python!”
def ejercicio1():
    print(len("Isto é Python!"))

# 2. Desmenuza o String “Python” mostrándoo por pantalla carácter a
# carácter.
def ejercicio2():
    palabra = "Python"
    for i in palabra:
        print(i)

# 3. Invertir o texto: “Python para todos”
def ejercicio3():
    print("Python para todos"[::-1])

# 4. Elimina os espazos do texto: “Guido Van Rossum creou Python”
def ejercicio4():
    print("Guido Van Rossum creou Python".replace(" ",""))

# 5. Conta as vocais e as consoantes do String “Python Python Python”.
# Ollo cos espazos!
def ejercicio5():

    vocales = []
    consonantes = []
    texto = "Python Python Python".lower().replace(' ','')

    for letra in texto:
        if letra.isalpha():
            if letra in "aeiou":
                vocales.append(letra)
            else:
                consonantes.append(letra)

    nvocales = len(vocales)
    nconsonantes = len(consonantes)

    print(f"Vocales: {nvocales} > {vocales}")
    print(f"Consonantes: {nconsonantes} > {consonantes}")

# 6. Divide a cadea de texto “ www. phytonparatodos. com” en duas partes “
# www. phyton” e “paratodos. com”. Para posteriormente concaténalas e
# mostralas de novo.
def ejercicio6():
    texto = "www. phytonparatodos. com"


# 7. Transforma a cadea de texto “ Phytoneros” a maiúsculas. Garda o valor
# na variable e posteriormente convértea novamente a minúsculas.
#
# 8. Compara se o String “Python” é igual que o String “ JavaScript”.
def ejercicio8():

    if "Python" == "JavaScript":
        print("Son iguales")
    else:
        print("No son iguales")

# 9. Sobre a cadea de texto “ Jeve jeve jeve”, substitúe todas as vocais e
# pola vogal para dando como resultado “java java java”.
def ejercicio9():

    texto = "Jeve jeve jeve"

    print(texto.replace('e', 'a'))

# 10. Tenta escribir un metodo, que dado un obxecto da clase str conte
# diferentes tipos de caracteres. En particular, o metodo deberá imprimir
# o número de letras, díxitos e espazos en branco da cadea. Tenta facer
# un programa que escriba o cálculo da cadea: «Ola, son alumno de
# DAM1, e son programador desde o 2025».
#
# 11.Escribir funcións que dada unha cadena de caracteres:
# a) Imprima os dous primeiros caracteres.
# b) Imprima os tres últimos caracteres.
# c) Imprima dita cadea cada dous caracteres. Ex.: recta debería imprimir
# rca
# d) Imprima a cadea nun sentido e en sentido inverso. Ex: reflexo imprime
# reflexooxelfer.
#
# 12. Escribir funcións que dada unha cadea e un caracter:
# a) Reemplace tódolos espazos polo caracter. Ex: ‘meu arquivo de
# texto.txt’ e ‘\_’ debería devoltar ‘meu\_arquivo\_de\_texto.txt’
# b) Inserte o caracter entre cada letra da cadea. Ex: ‘separar’ e ‘,’ debería
# devolver s,e,p,a,r,a,r
# c) Reemplace tódolos díxitos na cadea polo caracter. Ex: súa clave é:
# 1540 e ‘X’ debería devotar súa clave é: XXXX
#
# d) Inserte o caracter cada 3 díxitos na cadea. Ex. 2552552550 e ‘.’
# debería devoltar 255.255.255.0
#
# 13.Modificar as funcións anteriores, para que reciban un parámetro que indique
# a cantidade máxima de reemplazos ou insercións a realizar.
# 14.Escribir unha función que reciba unha cadea que conten un número entero
# longo e devolte unha cadea co número e as separacións de miles. Por
# exemplo, se recibe 1234567890, debe devoltar 1.234.567.890.
# 15.Escribir unha función que dada unha cadea de caracteres, devolte:
# i) A primeira letra de cada palabra. Por exemplo, si recibe Universal
# Serial Bus debe devoltar USB.
# ii) Unha cadea coa primeira letra de cada palabra en maiúsculas. Por
# exemplo, se recibe república arxentina, debe devoltar, República
# Argentina.
# iii) As palabras que comecen coa letra A. Por exemplo, si recibe Antes de
# abrir, debe devoltar, Antes abrir.
#
# 16.Escribir funcións que dada unha cadea de caracteres:
# a. Devolva soamente as letras consonantes. Por exemplo, se recibe
# ‘algoritmos’ ou ‘logaritmos’ debe devolver ‘lgrtms’.
# b. Devolva soamente as letras vogais. Por exemplo, se recibe ‘sen
# consonantes’ debe devoltar ‘e ooae’.
# c. Substitúa cada vogal pola súa seguinte vogal. Por exemplo, se recibe
# ‘vestiario’ debe devoltar ‘vostoerou’.
#
# 17.Indique si se trata dun palíndromo. Por exemplo, ‘anita lava la tina’ é un
# palíndromo (léese igual de esquerda a dereita que de dereita a esquerda).
#
# 18. Escribir funcións que dadas dúas cadeas de caracteres:
# a) Indique si a segunda cadea é unha subcadea da primeira. Por
# exemplo, ‘cadea’ é unha subcadea de ‘subcadea’.
#
# b) Devolva a que sexa anterior en orden alfábetico. Por exemplo, se
# recibe ‘kde' e ‘gnome’ debe devoltar ‘gnome’.
#
# 19.Escribir unha función que reciba unha cadea de uns e ceros (é dicir, un
# número en representación binaria) e devolte o valor decimal correspondente.
#
# 20. Escribir as seguintes funcións que fagan o seguinte:
# i) Recibindo unha cadea de caracteres e un caracter, retorne unha nova
# cadea formada exclusivamente polo novo caracter. Esta nova cadea
# tera a lonxitude da cadea pasada por parámetro.
# ii) Recibindo unha cadea de caracteres e un caracter, a función terá que
# comprobar si o caracter está na cadea. A función retornará un String
# no que aparezan guións e o caracter na posición ou posicións onde
# coincida na cadea.
#
# 21.Escribe a función que permita validar un contasinal, recibindo o contrasinal
# como parámetro. O contrasinal ten que cumprir as condicións de mínimo 8
# caracteres, o menos unha maiúscula, unha minúscula e un número. A función
# ten que retornar un booleano especificando si é válida ou non.
#
# 22.Escribe a función que permita formatear de nomes. A función ten que eliminar
# os espazos en branco e poñer en maiúsculas o primeiro caracter d o nome e
# apelido pasado como parámetro. Finalmente retornará unha cadea co nome
# e apelidos co formato solicitado.
#
# 23.Crear a función que permíta realizar un analisis simple de texto. O analizador
# ten a función de contar palabras, caracteres e encontrar a palabra mais
# longa. Mostrar os resultados por pantalla.

# 11.
"""
START
READ string
PRINT first 2 string characters
PRINT last 3 string characters
PRINT every 2 string characters
PRINT string characters start-end & end-start
END
"""
def boletin7_11():

    def print_first_two(cadena:str):
        print(cadena[:2]) #first 2 string characters

    def print_last_three(cadena: str):
        print(cadena[-3:]) #last 3 string characters

    def print_every_two(cadena: str):
        print(cadena[::2]) #every 2 string characters

    def print_normal_and_inverse(cadena: str):
        print(cadena + cadena[::-1]) #start-end & end-start

    cadena_main = 'Galicia'

    print_first_two(cadena_main)
    print_last_three(cadena_main)
    print_every_two(cadena_main)
    print_normal_and_inverse(cadena_main)

boletin7_11()