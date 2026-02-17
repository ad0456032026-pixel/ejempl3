Algoritmo Restar
	// solicitar al usuario 
	// que ingrese dos numeros enteros 
	// y mostrar la resta de ambos 
	Definir NumeroEntrada1, NumeroEntrada2, NumeroTotal Como Entero
	
	Escribir "Ingrese un numero para restar:"
	Leer NumeroEntrada1
	
	Escribir "Ingrese otro numero para restar: "
	Leer NumeroEntrada2
	
	si NumeroEntrada1>= NumeroEntrada2 Entonces
		resultado = NumeroEntrada1 - NumeroEntrada2
		Escribir "La resta es: " , resultado 
	Sino 
		Escribir "Error: El primer numero debe ser mayor que el segundo numero para evitar resultados negativos. "
	FinSi
	
FinAlgoritmo
