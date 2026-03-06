Algoritmo Ejercicio9CondidionOR
	
	Definir numeroIngresado Como Entero
	
	Escribir "Validador de divisibilidad "
	Escribir "Ingrese un numero entero para evaluar" 
	Leer numeroIngresado
	
	// utilizamos MOD, calcula el RESIDUO de una división entera.
	
	Si (numeroIngresado MOD 3 = 0) O (numeroIngresado MOD 5 = 0) Entonces
        Escribir "Verdadero"
	
        Si (numeroIngresado MOD 3 = 0) Y (numeroIngresado MOD 5 = 0) Entonces
            Escribir "El numero es divisible por AMBOS (3 y 5)."
        SiNo
            Si numeroIngresado MOD 3 = 0 Entonces
                Escribir "El numero es divisible solo por 3."
            SiNo
                // Si entró al primer SI, pero no es ambos, y no es el 3, por descarte es el 5
                Escribir "El número es divisible solo por 5."
            FinSi
        FinSi
        
    SiNo
        Escribir "Falso (El número no es divisible ni por 3 ni por 5)."
    FinSi
FinAlgoritmo
