print('\nBoletín 7.')



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