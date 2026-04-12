texto = "pYTHON"

texto_invertido = texto.swapcase()

texto_alineado = texto_invertido.ljust(15, "*")

# resultados
print("Texto original:", texto)
print("Texto con capitalización invertida:", texto_invertido)
print("Texto final alineado:", texto_alineado)
