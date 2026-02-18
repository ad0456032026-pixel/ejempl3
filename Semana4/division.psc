Algoritmo division
	// solicitar al usuario 
	// que ingrese dos numeros enteros 
	// y mostrar la division del primero entre el segundo
	Definir NumeroEntrada1, NumeroEntrada2, resultado Como Real 
	
	Escribir "Ingrese el numero a dividir: "
	Leer NumeroEntrada1
	
	Escribir "Ingrese el divisor: "
	Leer NumeroEntrada2
	
	Si NumeroEntrada2 > 0 Entonces
		resultado = NumeroEntrada1 / NumeroEntrada2
		Escribir "El resultado de la division es: " , resultado
	SiNo
		Escribir  "Error: no se puede dividir entre 0. "
	FinSi
	
	
FinAlgoritmo
