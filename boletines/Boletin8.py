def salir():
    """
    Salir del menú de una forma más visual.
    """
    print("\n👋 Saliendo del menú del Boletín 8...")
    return False

OPCIONES_MENU = {
    "1":  ("", ),
    "2":  ("", ),
    "3":  ("", ),
    "4":  ("", ),
    "5":  ("", ),
    "0":  ("Salir", salir)
}

def menu_boletin8():
    """
    Despliega el menú principal del boletín y gestiona la navegación.

    Utiliza un patrón Dispatcher con diccionario para seleccionar
    la función correspondiente a cada ejercicio.

    :return: None
    """
    continuar = True
    
    while continuar:
        print("\n--- Menú de Ejercicios Boletín 8 ---")
        
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
    menu_boletin8()