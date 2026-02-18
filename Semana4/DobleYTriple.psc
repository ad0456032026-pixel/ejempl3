Algoritmo DobleYTriple
	// solicitar al usuario
	// que ingrese un numero distinto de 0
	// y mostrar su doble y triple
	Definir Numero1, doble, triple Como Real
	
	Escribir "Ingrese un numero distinto de cero: "
	Leer Numero1
	
	Si Numero1 > 0 Entonces
		doble = Numero1 * 2
		triple = Numero1 * 3
		Escribir "Doble: " , doble, "| Triple: " , triple
	SiNo
		Escribir "Ingresaste cero, su doble y triple seguiran siendo cero. "
	FinSi
	
FinAlgoritmo
