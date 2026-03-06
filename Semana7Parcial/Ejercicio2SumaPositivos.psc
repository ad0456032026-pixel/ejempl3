Algoritmo Ejercicio2SumaPositivos
	Definir numero1, suma Como Real
	suma <- 0 
	
	Escribir "Sumacion de numeros positivos "
	Repetir
		Escribir "ingrese un numero (INGRESE UN NEGATIVO PARA TERMINAR): "
		Leer numero1
		si numero1 >= 0 Entonces
			suma <- suma + numero1
		FinSi
	Hasta Que numero1 < 0 
	Escribir "La suma de todos los numeros positivos es: ", suma
FinAlgoritmo
