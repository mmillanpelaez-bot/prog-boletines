
def ejercicio1():
    """
    1. Mostra a lonxitude do texto: “ Isto é Python!
    ”"""
    print(len("Isto é Python!"))


def ejercicio2():
    """
    2. Desmenuza o String “Python” mostrándoo por pantalla carácter a carácter.
    """
    palabra = "Python"
    for i in palabra:
        print(i)


def ejercicio3():
    """
    3. Invertir o texto: “Python para todos”
    """
    print("Python para todos"[::-1])


def ejercicio4():
    """
    4. Elimina os espazos do texto: “Guido Van Rossum creou Python”
    """
    print("Guido Van Rossum creou Python".replace(" ",""))


def ejercicio5():
    """
    5. Conta as vocais e as consoantes do String “Python Python Python”. Ollo cos espazos!
    """
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


def ejercicio6():
    """
    6. Divide a cadea de texto “ www. phytonparatodos. com” en duas partes “ www. phyton” e “paratodos. com”. Para posteriormente concaténalas e mostralas de novo.
    """
    text = "www. phytonparatodos. com"
    part1 = text[0:11]
    part2 = text[11:]
    text_reconstruct = part1 + part2

    print(f'Primera parte: {part1}')
    print(f'Segunda parte: {part2}')
    print(f'Resultado final: {text_reconstruct}')


def ejercicio7():
    """
    7. Transforma a cadea de texto “ Phytoneros” a maiúsculas. Garda o valor na variable e posteriormente convértea novamente a minúsculas.
    """
    ucase = "Phytoneros".upper()
    lcase = "Phytoneros".lower()

    print(ucase)
    print(lcase)


def ejercicio8():
    """
    8. Compara se o String “Python” é igual que o String “ JavaScript”.
    """
    if "Python" == "JavaScript":
        print("Son iguales")
    else:
        print("No son iguales")


def ejercicio9():
    """
    9. Sobre a cadea de texto “ Jeve jeve jeve”, substitúe todas as vocais e pola vogal para dando como resultado “java java java”.
    """
    texto = "Jeve jeve jeve"

    print(texto.replace('e', 'a'))


def ejercicio10():
    """
    10. Tenta escribir un metodo, que dado un obxecto da clase str conte diferentes tipos de caracteres. En particular, o metodo deberá imprimir o número de letras, díxitos e espazos en branco da cadea. Tenta facer un programa que escriba o cálculo da cadea: «Ola, son alumno de DAM1, e son programador desde o 2025».
    """
    def count_characters(string: str) -> None:
        letters = 0
        digits = 0
        spaces = 0

        for char in string:
            if char.isalpha():
                letters += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1

        print(f"Letras: {letters}")
        print(f"Dígitos: {digits}")
        print(f"Espacios: {spaces}")

    text = "Ola, son alumno de DAM1, e son programador desde o 2025"
    count_characters(text)

def ejercicio11():
    """
     11.Escribir funcións que dada unha cadena de caracteres:
      a) Imprima os dous primeiros caracteres.
      b) Imprima os tres últimos caracteres.
      c) Imprima dita cadea cada dous caracteres. Ex.: recta debería imprimir rca.
      d) Imprima a cadea nun sentido e en sentido inverso. Ex: reflexo imprime reflexooxelfer.
    """
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


def ejercicio12():
    """
    12. Escribir funcións que dada unha cadea e un caracter:
    a) Reemplace tódolos espazos polo caracter. Ex: ‘meu arquivo de texto.txt’ e ‘\_’ debería devoltar ‘meu\_arquivo\_de\_texto.txt’
    b) Inserte o caracter entre cada letra da cadea. Ex: ‘separar’ e ‘,’ debería devolver s,e,p,a,r,a,r
    c) Reemplace tódolos díxitos na cadea polo caracter. Ex: súa clave é: 1540 e ‘X’ debería devotar súa clave é: XXXX
    d) Inserte o caracter cada 3 díxitos na cadea. Ex. 2552552550 e ‘.’ debería devoltar 255.255.255.0
    """
    def replace_spaces(text: str, char: str) -> str:
        """a) Reemplace tódolos espazos polo caracter. Ex: ‘meu arquivo de texto.txt’ e ‘\_’ debería devoltar ‘meu\_arquivo\_de\_texto.txt’"""
        return text.replace(" ", char)

    def insert_char(text: str, char: str) -> str:
        """b) Inserte o caracter entre cada letra da cadea. Ex: ‘separar’ e ‘,’ debería devolver s,e,p,a,r,a,r"""
        for char in text:
            text.join(char)


    print(replace_spaces("meu arquivo de texto.txt", "\_"))
    print(insert_char("separar", ","))


def ejercicio13():
    """
    13.Modificar as funcións anteriores, para que reciban un parámetro que indique a cantidade máxima de reemplazos ou insercións a realizar.
    """
    pass


def ejercicio14():
    """
    14.Escribir unha función que reciba unha cadea que conten un número entero longo e devolte unha cadea co número e as separacións de miles. Por exemplo, se recibe 1234567890, debe devoltar 1.234.567.890.
    """
    pass


def ejercicio15():
    """
    15.Escribir unha función que dada unha cadea de caracteres, devolte:
    i) A primeira letra de cada palabra. Por exemplo, si recibe Universal Serial Bus debe devoltar USB.
    ii) Unha cadea coa primeira letra de cada palabra en maiúsculas. Por exemplo, se recibe república arxentina, debe devoltar, República Argentina.
    iii) As palabras que comecen coa letra A. Por exemplo, si recibe Antes de abrir, debe devoltar, Antes abrir.
    """
    pass


def ejercicio16():
    """
    16.Escribir funcións que dada unha cadea de caracteres:
    a. Devolva soamente as letras consonantes. Por exemplo, se recibe ‘algoritmos’ ou ‘logaritmos’ debe devolver ‘lgrtms’.
    b. Devolva soamente as letras vogais. Por exemplo, se recibe ‘sen consonantes’ debe devoltar ‘e ooae’.
    c. Substitúa cada vogal pola súa seguinte vogal. Por exemplo, se recibe ‘vestiario’ debe devoltar ‘vostoerou’.
    """
    pass


def ejercicio17():
    """
    17.Indique si se trata dun palíndromo. Por exemplo, ‘anita lava la tina’ é un palíndromo (léese igual de esquerda a dereita que de dereita a esquerda).
    """
    pass


def ejercicio18():
    """18. Escribir funcións que dadas dúas cadeas de caracteres:
    a) Indique si a segunda cadea é unha subcadea da primeira. Por exemplo, ‘cadea’ é unha subcadea de ‘subcadea’.
    b) Devolva a que sexa anterior en orden alfábetico. Por exemplo, se recibe ‘kde' e ‘gnome’ debe devoltar ‘gnome’.
    """
    pass


def ejercicio19():
    """
    19.Escribir unha función que reciba unha cadea de uns e ceros (é dicir, un número en representación binaria) e devolte o valor decimal correspondente.
    """
    pass


def ejercicio20():
    """
    20. Escribir as seguintes funcións que fagan o seguinte:
    i) Recibindo unha cadea de caracteres e un caracter, retorne unha nova cadea formada exclusivamente polo novo caracter. Esta nova cadea tera a lonxitude da cadea pasada por parámetro.
    ii) Recibindo unha cadea de caracteres e un caracter, a función terá que comprobar si o caracter está na cadea. A función retornará un String no que aparezan guións e o caracter na posición ou posicións onde coincida na cadea.
    """
    pass


def ejercicio21():
    """
    21.Escribe a función que permita validar un contasinal, recibindo o contrasinal como parámetro. O contrasinal ten que cumprir as condicións de mínimo 8 caracteres, o menos unha maiúscula, unha minúscula e un número. A función ten que retornar un booleano especificando si é válida ou non.
    """
    pass


def ejercicio22():
    """
    22.Escribe a función que permita formatear de nomes. A función ten que eliminar os espazos en branco e poñer en maiúsculas o primeiro caracter d o nome e apelido pasado como parámetro. Finalmente retornará unha cadea co nome e apelidos co formato solicitado.
    """
    pass


def ejercicio23():
    """
    23.Crear a función que permíta realizar un analisis simple de texto. O analizador ten a función de contar palabras, caracteres e encontrar a palabra mais longa. Mostrar os resultados por pantalla.
    """
    pass


def salir():
    """
    Salir del menú de una forma más visual.
    """
    print("\n👋 Saliendo del menú del Boletín 7...")
    return False

OPCIONES_MENU = {
    "1" : ("", ejercicio1),
    "2" : ("", ejercicio2),
    "3" : ("", ejercicio3),
    "4" : ("", ejercicio4),
    "5" : ("", ejercicio5),
    "6" : ("", ejercicio6),
    "7" : ("", ejercicio7),
    "8" : ("", ejercicio8),
    "9" : ("", ejercicio9),
    "10": ("", ejercicio10),
    "11": ("", ejercicio11),
    "12": ("", ejercicio12),
    "13": ("", ejercicio13),
    "14": ("", ejercicio14),
    "15": ("", ejercicio15),
    "16": ("", ejercicio16),
    "17": ("", ejercicio17),
    "18": ("", ejercicio18),
    "19": ("", ejercicio19),
    "20": ("", ejercicio20),
    "21": ("", ejercicio21),
    "22": ("", ejercicio22),
    "23": ("", ejercicio23),
    "0":  ("Salir", salir)
}

def menu_boletin7():
    """
    Despliega el menú principal del boletín y gestiona la navegación.

    Utiliza un patrón Dispatcher con diccionario para seleccionar
    la función correspondiente a cada ejercicio.

    :return: None
    """
    continuar = True
    
    while continuar:
        print("\n--- Menú de Ejercicios Boletín 7 ---")
        
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
    menu_boletin7()