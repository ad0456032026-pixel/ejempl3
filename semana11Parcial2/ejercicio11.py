texto = "  el nido matinal  "

texto_limpio = texto.strip().title()

texto_centrado = texto_limpio.center(30, "-")

#  los resultados
print("Texto original:", f"'{texto}'")
print("Texto limpio y en título:", f"'{texto_limpio}'")
print("Texto final centrado:", texto_centrado)
