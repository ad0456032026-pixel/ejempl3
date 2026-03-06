Algoritmo Ejercicio10MayorMenorIgual
	
	Definir primerNumero, segundoNumero Como Real
	
	Escribir "Comparador de numeros "
	Escribir "Ingrese el primer numero: "
	Leer primerNumero
	
	Escribir "Ingrese el segundo numero: "
	Leer segundoNumero
	
	Si primerNumero > segundoNumero Entonces
        Escribir "El primer número (", primerNumero, ") es MAYOR que el segundo (", segundoNumero, ")."
    SiNo
        
        Si primerNumero < segundoNumero Entonces
            Escribir "El primer número (", primerNumero, ") es MENOR que el segundo (", segundoNumero, ")."
        SiNo
            // Si la computadora llega hasta aquí, significa que no es ni mayor ni menor
			
            Escribir "Ambos números son IGUALES (", primerNumero, ") igual a (", segundoNumero, ")."
        FinSi
    FinSi
FinAlgoritmo
