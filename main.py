import os
from boletines.boletin1.main1 import menu_boletin1
from boletines.boletin2.main2 import menu_boletin2
from boletines.boletin3.main3 import menu_boletin3
from boletines.boletin4.main4 import menu_boletin4
from boletines.boletin5.main5 import menu_boletin5
from boletines.boletin6.main6 import menu_boletin6
from boletines.boletin7.main7 import menu_boletin7
from boletines.boletin8.main8 import menu_boletin8



def limpiar_pantalla():
    """Detecta el sistema operativo y limpia la terminal."""
    if os.name == 'nt':      # Si es Windows
        os.system('cls')
    else:                    # Si es Linux/Mac
        os.system('clear')


def salir():
    print("\n👋 Saliendo del menú principal Boletines...")
    return False

OPCIONES_MENU = {
    "1":  ("Boletín 1: Expresiones y booleanos", menu_boletin1),
    "2":  ("Boletín 2: Algorítmia", menu_boletin2),
    "3":  ("Boletín 3: Condicionales", menu_boletin3),
    "4":  ("Boletín 4: Condicionales", menu_boletin4),
    "5":  ("Boletín 5: Bucles", menu_boletin5),
    "6":  ("Boletín 6: Listas y Tuplas", menu_boletin6),
    # "7":  ("Boletín 7: Cadenas de caracteres", menu_boletin7),
    # "8":  ("Boletín 8: Tuplas, listas y diccionarios", menu_boletin8),
    "0":  ("Salir", salir)
}

def menu_boletines():
    """
        Despliega el menú principal de los boletines y gestiona la navegación.

        Utiliza un patrón Dispatcher con diccionario para seleccionar
        la función correspondiente a cada ejercicio.

        :return: None
        """
    continuar = True
    
    while continuar:
        print("\n--- Menú principal Boletines ---")
        
        for clave, valor in OPCIONES_MENU.items():
            descripcion = valor[0]
            print(f"{clave}. {descripcion}")

        choice = input("\n>> Seleccione un Boletín: ")


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
    menu_boletines()