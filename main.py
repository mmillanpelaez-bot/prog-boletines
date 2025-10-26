"""
needs some polish:
-imports at the top-
less if statements
automate
make scalable
diccionary
"""
from boletines.Boletin1 import menu_boletin1
from boletines.Boletin2 import menu_boletin2
#from boletines.Boletin3 import menu_boletin3
#from boletines.Boletin4 import menu_boletin4
#from boletines.Boletin5 import menu_boletin5
#from boletines.Boletin6 import menu_boletin6
#from boletines.Boletin7 import menu_boletin7
#from boletines.Boletin8 import menu_boletin8

def menu_boletines():
    print("\n--- Menú de Boletines ---")
    print("1. Boletín 1: Expresiones y booleanos")
    print("2. Boletín 2: Algorítmia")
    print("3. Boletín 3: Condicionales")
    print("4. Boletín 4: Condicionales")
    print("5. Boletín 5: Bucles")
    print("6. Boletín 6: Listas y Tuplas")
    print("7. Boletín 7: Cadenas de caracteres")
    print("8. Boletín 8: Tuplas, listas y diccionarios")
    print("0. Salir")

    choice = input("Seleccione un boletín: ")

    if choice == '1':
        menu_boletin1()
    elif choice == '2':
        menu_boletin2()
    # elif choice == '3':
    #     menu_boletin3()
    # elif choice == '4':
    #     menu_boletin4()
    # elif choice == '5':
    #     menu_boletin5()
    # elif choice == '6':
    #     menu_boletin6()
    # elif choice == '7':
    #     menu_boletin7()
    # elif choice == '8':
    #     menu_boletin8()
    elif choice == '0':
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Inténtelo de nuevo.")
        
menu_boletines()