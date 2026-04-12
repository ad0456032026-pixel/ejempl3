texto = "Bryan Alas"

texto_normalizado = texto.casefold()

es_solo_letras = texto_normalizado.isalpha()

# resultaos
print("Texto original:", texto)
print("Texto normalizado:", texto_normalizado)
print("¿Está compuesto solo por letras?:", es_solo_letras)
