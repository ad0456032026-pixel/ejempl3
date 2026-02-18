Algoritmo CalculadoraCompleta
	Definir Numero1, Numero2 Como Real
	
	// solicitar al usuario 
	// que ingrese dos numeros y mostrar la
	// suma, resta, multiplicacion y division de ambos
	
	Escribir "Ingrese dos numeros: "
	Leer Numero1, Numero2
	
	Escribir "Suma: " , Numero1 + Numero2
	Escribir "Resta: " , Numero1 - Numero2
	Escribir "Multiplicacion: " , Numero1 * Numero2 
	
	Si Numero2 <> 0 Entonces
		Escribir "Dision: " , Numero1 / Numero2
	SiNo
		Escribir "D	ivison: No definida, no se puede dividir entre cero. "
	FinSi
	
FinAlgoritmo
