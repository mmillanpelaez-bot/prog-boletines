
def salir():
    print("\n👋 Saliendo del menú del Boletín 6...")
    return False

OPCIONES_MENU = {
    "1":  ("Imprimir rango de números", ejercicio1),
    "2":  ("Conversor Fahrenheit > Celsius", ejercicio2),
    "3":  ("Tabla conversion temperatura", ejercicio3),
    "4":  ("Numeros pares", ejercicio4),
    "5":  ("Primer numero triangular", ejercicio5),
    "6":  ("Calcular factorial", ejercicio6),
    "7":  ("Fichas domino.", ejercicio7),
    "8":  ("Reutilizar fichas", ejercicio8),
    "9":  ("Calcular numeros negativos", ejercicio9),
    "10": ("Calcular area rectangulo", ejercicio10),
    "11": ("Tabla de multiplicar de n", ejercicio11),
    "12": ("Rango sueldo trabajadores", ejercicio12),
    "13": ("Dibujo triangulo base n", ejercicio13),
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