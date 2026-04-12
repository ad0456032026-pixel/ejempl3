texto = "Python2026"

es_alfanumerico = texto.isalnum()

if es_alfanumerico:
    texto_minusculas = texto.lower()

    texto_final = texto_minusculas.replace("2026", "")

    # mmuestra los resultados si se cumple
    print("Texto original:", texto)
    print("¿Es estrictamente alfanumérico?:", es_alfanumerico)
    print("Texto en minúsculas:", texto_minusculas)
    print("Texto final separado:", texto_final)
else:
    print("El texto no es estrictamente alfanumérico.")
