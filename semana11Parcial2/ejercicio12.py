archivo = "ING. Bryan Alas.txt"

sin_sufijo = archivo.removesuffix(".txt")
sin_prefijo = sin_sufijo.removeprefix("ING. ")

texto_minusculas = sin_prefijo.lower()
lista_final = texto_minusculas.split()

# resultados
print("Nombre de archivo original:", archivo)
print("Texto limpio en minúsculas:", texto_minusculas)
print("Lista final generada:", lista_final)
