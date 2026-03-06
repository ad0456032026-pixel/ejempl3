Algoritmo Ejercicio3DiaSemana
	
	Definir dia Como Entero
	
	Escribir "Dias de la semana"

	Repetir 
		Escribir "Ingrese un numero de el 1 al 7: "
		Leer dia
	 
	  // La estructura SEGUN evalua el valor exacto de la variable
	 
	 Segun dia Hacer
        1: 
            Escribir "El dia 1 es: Lunes "
        2: 
            Escribir "El dia 2 es: Martes "
        3: 
            Escribir "El dia 3 es: Miércoles "
        4: 
            Escribir "El dia 4 es: Jueves "
        5: 
            Escribir "El dia 5 es: Viernes "
        6: 
            Escribir "El dia 6 es: Sábado "
        7: 
            Escribir "El dia 7 es: Domingo "
        De Otro Modo:
            // Este es el caso para manejar cualquier número que no sea del 1 al 7, como el 8
            Escribir "Numero invalido, solo se aceptan valores entre 1 y 7, intente de nuevo."
     FinSegun
     Hasta Que dia	>= 1 y dia <= 7 
FinAlgoritmo
