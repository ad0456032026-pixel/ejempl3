Algoritmo bucleSFB
	// un bucle es algo que se repite hasta que
	// una condicion logica la rompe 
	
	Definir contador, numeroEntrada, anterior, resultado  Como Entero
	Escribir " numero del 0 al 100 " 
	Leer numeroEntrada 
	anterior = 0
	resultado = 1 
	contador = 2
	

	Mientras contador < numeroEntrada 
		nuevo = anterior + resultado
		Escribir "resultado es: " , anterior ," + " , resultado, " = ", nuevo
		anterior = resultado
		resultado = nuevo
		contador = contador + 1
		
		
	FinMientras

	
	

	// gerarquia 
	
	// contador i  i++ i--  

	
	
	
FinAlgoritmo
