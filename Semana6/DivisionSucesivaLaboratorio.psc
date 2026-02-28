Algoritmo DivisionSucesivaLaboratorio
	Definir MiNumero Como Real
	Definir paso1 Como Entero
	Definir entradaValida, terminarCiclo Como Logico
	
	paso1 <- 0 
	terminarCiclo <- Falso
	
	Escribir "= Laboratorio 01: División Sucesiva ="
	
	// ciclo 1
	Repetir
		
		Escribir " Ingrese un numero estrictamente mayor que 1 para realizar la division: "
		Leer MiNumero
		
		si (MiNumero > 1 ) y no ( MiNumero <= 0) Entonces
			entradaValida <- Verdadero
		SiNo
			Escribir " error, escribiste un numero menor que 1, intenta de nuevo"
			entradaValida <- Falso
			
		FinSi
		
	Hasta Que entradaValida = Verdadero 
	
	Escribir " numero aceptado, comenzando a dividir "
	
    // ciclo 2
	Mientras terminarCiclo = Falso Hacer
		
		 
		MiNumero <- MiNumero / 2
		paso1 <- paso1 + 1 
		Escribir " paso " , paso1, ": El numero ahora es: " , MiNumero
		
		si (MiNumero < 1) O (MiNumero == 0) Entonces
			terminarCiclo <-  Verdadero
		SiNo
			terminarCiclo <- Falso
		FinSi
		
	FinMientras
	
	Escribir " proceso terminado, el numero ya es menor que 1. "
FinAlgoritmo
