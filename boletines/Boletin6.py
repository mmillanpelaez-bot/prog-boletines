print('\nBoletín 6.')






def salir():
    print("\n👋 Saliendo del menú del Boletín 6...")
    return False # Retornamos False para indicar que queremos parar el bucle

# --- 2. Configuración del Menú ---
# Estructura: "Clave": ("Descripción para el usuario", referencia_a_la_funcion)
# NOTA: No uses paréntesis () en las funciones aquí, solo el nombre.
OPCIONES_MENU = {
    "1":  ("Ejercicio 1", ejercicio1),
    "2":  ("Ejercicio 2", ejercicio2),
    "3":  ("Ejercicio 3", ejercicio3),
    "4":  ("Ejercicio 4", ejercicio4),
    "5":  ("Ejercicio 5", ejercicio5),
    "6":  ("Ejercicio 6", ejercicio6),
    "7":  ("Ejercicio 7", ejercicio7),
    "8":  ("Ejercicio 8", ejercicio8),
    "9":  ("Ejercicio 9", ejercicio9),
    "10": ("Ejercicio 10", ejercicio10),
    "11": ("Ejercicio 11", ejercicio11),
    "12": ("Ejercicio 12", ejercicio12),
    "13": ("Ejercicio 13", ejercicio13),
    "0":  ("Salir", salir)
}

def menu_boletin6():
    continuar = True
    
    while continuar:
        print("\n--- Menú de Ejercicios Boletín 6 ---")
        
        # Bucle de visualización: Generamos la lista dinámicamente
        # Esto es lo que lo hace escalable. Si añades el 14 arriba, sale solo aquí.
        for clave, valor in OPCIONES_MENU.items():
            descripcion = valor[0]
            print(f"{clave}. {descripcion}")

        choice = input("\n>> Seleccione un ejercicio: ")

        # Lógica de despacho (Dispatcher)
        if choice in OPCIONES_MENU:
            accion = OPCIONES_MENU[choice][1] # Obtenemos la función
            
            try:
                # Ejecutamos la función. 
                # Capturamos el retorno por si es la función salir()
                resultado = accion() 
                
                # Si la función devuelve explícitamente False (como salir), rompemos
                if resultado is False:
                    continuar = False
                else:
                    input("\n[Intro para continuar...]") # Pausa táctica para leer el resultado
                    
            except NameError:
                print(f"⚠️  Error: La función {accion.__name__} no está definida todavía.")
            except Exception as e:
                print(f"⚠️  Ocurrió un error inesperado en el ejercicio: {e}")
                
        else:
            print("❌ Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    # Necesitas tener definidas las funciones ejercicio1...ejercicio13 
    # para que esto no falle al elegir una opción.
    menu_boletin6()