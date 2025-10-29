def ejercicio5():
    texto = "Python Python Python".lower().replace(" ", "")
    vocales = []
    consonantes = []

    for letra in texto:
        if letra.isalpha():
            if letra in "aeiou":
                vocales.append(letra)
            else:
                consonantes.append(letra)

    print(f"Vogais: {len(vocales)} → {vocales}")
    print(f"Consoantes: {len(consonantes)} → {consonantes}")
ejercicio5()