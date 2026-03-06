Algoritmo Ejercicio5Bucle1a10
	Definir numeroIngresado Como Real
	
	Escribir "Juego del rango (1 al 10) "
	Escribir "Ingrese un numero entre 1 y 10: "
	Leer numeroIngresado
	
	// El bucle MIENTRAS evalúa la condición ANTES de entrar
    Mientras numeroIngresado >= 1 Y numeroIngresado <= 10 Hacer
        Escribir "Excelente, el numero ", numeroIngresado, " es valido "
        
        // es obligatorio volver a pedir el número DENTRO del bucle, 
        // si no lo hacemos el bucle se repetiría infinitamente
        Escribir "Ingrese otro numero entre 1 y 10 (o un numero fuera del rango para salir): "
        Leer numeroIngresado
    FinMientras
    
    // Si el programa llega a esta línea, es porque la condición del Mientras no se cumplió
    Escribir "¡Ups! Ha ingresado un numero invalido"
    Escribir "Fin del juego."
	
FinAlgoritmo
