palabra = "CANTANDO"

palabra_minusculas = palabra.lower()

sin_sufijo = palabra_minusculas.removesuffix("ando")

indice_t = sin_sufijo.find("t")

# resultadiños
print("Palabra original:", palabra)
print("En minúsculas:", palabra_minusculas)
print("Sin el sufijo:", sin_sufijo)
print("El índice de la letra 't' es:", indice_t)
