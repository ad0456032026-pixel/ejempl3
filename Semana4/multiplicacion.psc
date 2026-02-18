Algoritmo multiplicacion
	// solicitar al usuario 
	// que ingrese dos numeros enteros 
	// y mostrar la multiplicacion de ambos
	
	Definir NumeroEntrada1, NumeroEntrada2, NumeroTotal Como Real 
	
	Escribir "Ingrese un numero para multiplicar: "
	Leer NumeroEntrada1
	
	Escribir "Ingrese otro numero para multiplicar: "
	Leer NumeroEntrada2
	
	Si NumeroEntrada1 > 0 y NumeroEntrada2 > 0 Entonces
		resultado = NumeroEntrada1 * NumeroEntrada2 
		Escribir "El resultado es: " , resultado
	SiNo
		Escribir "Ingresaste un 0, todo numero multiplicado por 0 es 0. "
	FinSi
	
FinAlgoritmo
