Algoritmo Ejercicio4Pares
	Definir CantidadDePares, contador Como Entero
	
	Escribir "Generador de numeros pares"
	
	Repetir
		Escribir "Ingrese la cantidad de numeros pares que desea ver: "
		Leer CantidadDePares
		
		Si CantidadDePares <= 0 Entonces
			Escribir "Error, debe ingresar un numero mayor que 0, intente de nuevo "
		FinSi
		
	Hasta Que CantidadDePares > 0 
	
	Escribir "Los primeros ", CantidadDePares, " numeros pares son: "
	Para contador <- 1 Hasta cantidadDePares Con Paso 1 Hacer
		Escribir contador * 2
	FinPara
FinAlgoritmo
