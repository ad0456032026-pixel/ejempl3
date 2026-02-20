Algoritmo password
	
	Definir pass, respuesta como cadena 
	pass = ""
	
	Mientras pass <> "nombre de ella + fecha especial"
		Escribir "ingresa password"
		leer pass 
		
		si  pass <> "nombre de ella + fecha epecial" Entonces
			Escribir "romper bucle infinito si o no"
			leer respuesta
			si respuesta == "si" Entonces
				pass = "nombre de ella + fecha especial"
				
			FinSi
			si respuesta == "no" Entonces
				Escribir "sigue intentando"
			FinSi
		FinSi
		
		
	FinMientras
	
	Escribir "final "
FinAlgoritmo
