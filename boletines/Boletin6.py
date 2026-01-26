# Boletín 6. Listas e tuplas

# 1. Escribir un programa que almacene as asignaturas dun
# curso (por exemplo Matemáticas, Física, Química, Historia
# e Língua) nunha lista, pregunte o usuario a nota que
# sacou en cada asignatura, e despois as mostre por
# pantalla co mensaxe En <asignatura> sacaches <nota>
# onde <asignatura> é cada unha das asignaturas da lista e
# <nota> cada unha das correspondentes notas
# introducidas polo usuario.
def ejercicio1():
    print("\n--- Ejercicio 1 ---")
    print("\nAlmacenar y mostrar")

    asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Língua']
    notas = []

    for asignatura in asignaturas:
        nota = input(f"\nIntroduce a nota que sacaches en {asignatura}: ")
        notas.append(nota)

    for i in range(len(asignaturas)):
        print(f"\nEn {asignaturas[i]} sacaches {notas[i]}")

# 2. Escribir un programa que pregunte o usuario os números
# gañadores da lotería primitiva, os almacene nunha lista e
# os muestre por pantalla ordenados de menor a maior.
def ejercicio2():
    print("\n--- Ejercicio 2 ---")
    print("\nAlmacenar y mostrar lista de menor a mayor")

# 3. Escribir un programa que almacene nunha lista os
# números do 1 o 10 e os mostre por pantalla en orden
# inverso separados por comas.
def ejercicio3():
    print("\n--- Ejercicio 3 ---")
    print("\nAlmacenar y mostrar lista inversa en un rango")

# 4. Escribir un programa que almacene as asignaturas dun
# curso (por exemplo Matemáticas, Física, Química, Historia
# e Língua) nunha lista, pregunte o usuario a nota que
# sacou en cada asignatura e elimine da lista as asignaturas
# aprobadas. O fin, o programa debe mostrar por pantalla
# as asignaturas que o usuario ten que repetir.
def ejercicio4():
    print("\n--- Ejercicio 4 ---")
    print("\nAlmacenar, mostrar y eliminar de una lista ")
    ejercicio1()
# 5. Escribir un programa que almacene o abecedario nunha
# lista, e cree outra lista a partir dela, onde non aparezan as
# letras que ocupen posicións múltiplos de 3, e mostre por
# pantalla a lista resultante.


# 6. Escribir un programa que pida o usuario unha palabra e
# mostre por pantalla si é un palíndromo.


# 7. Escribir un programa que pida o usuario unha palabra e
# mostre por pantalla o número de veces que conten cada
# vogal.


# 8. Escribir un programa que almacene nunha lista os
# seguintes prezos, 50, 75, 46, 22, 80, 65, 8, e mostre por
# pantalla o menor e o maior dos prezos.


# 9. Escribir un programa que almacene os vectores (1,2,3) e
# (-1,0,2) en duas listas e mostre por pantalla o seu
# producto escalar.


# 10. Escribir un programa que almacene as matrices
# a = (1,2,3) b = (-1,0)
# (4,5,6) (0,1)
# (1,1)
# nunha lista e mostre por pantalla o seu produto.
# Nota: Para representar matrices mediante listas usar listas
# anidadas, representando cada vector fila nunha tupla


# 11. Escribir un programa que pregunte por unha mostra de
# números, separados por comas, os garde nunha lista e mostre
# por pantalla a súa media e desviación típica.



def salir():
    print("\n👋 Saliendo del menú del Boletín 6...")
    return False

OPCIONES_MENU = {
    "1":  ("Almacenar y mostrar lista", ejercicio1),
     "2":  ("Almacenar y mostrar lista de menor a mayor", ejercicio2),
     "3":  ("Almacenar y mostrar lista inversa en un rango", ejercicio3),
     "4":  ("Almacenar, mostrar y eliminar de la lista", ejercicio4),
    # "5":  ("Primer numero triangular", ejercicio5),
    # "6":  ("Calcular factorial", ejercicio6),
    # "7":  ("Fichas domino.", ejercicio7),
    # "8":  ("Reutilizar fichas", ejercicio8),
    # "9":  ("Calcular numeros negativos", ejercicio9),
    # "10": ("Calcular area rectangulo", ejercicio10),
    # "11": ("Tabla de multiplicar de n", ejercicio11),
    # "12": ("Rango sueldo trabajadores", ejercicio12),
    # "13": ("Dibujo triangulo base n", ejercicio13),
    "0":  ("Salir", salir)
}

def menu_boletin6():
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