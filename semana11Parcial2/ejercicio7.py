numero = "42"

numero_relleno = numero.zfill(5)

termina_en_dos = numero_relleno.endswith("2")

# los resultados
print("Número original:", numero)
print("Número con relleno de ceros:", numero_relleno)
print("¿El número termina en '2'?:", termina_en_dos)
