Algoritmo Ejercicio1Calificacion
	Definir nota Como Real 

	// validar la nota
	Repetir
        Escribir "Ingrese la nota del estudiante (0 a 10): "
        Leer nota
        
        Si nota < 0 O nota > 10 Entonces
            Escribir "Error: Nota inválida. Por favor, intente de nuevo."
            Escribir "------------------------------------------------"
        FinSi
    Hasta Que nota >= 0 Y nota <= 10
	
	Si nota >= 6 Entonces
		Escribir "Calificacion: Aprobado "
	SiNo
		Si nota >= 5 Entonces
			Escribir "Calificacion: Recuperacion "
		SiNo
			Escribir "Calificacion: Reprobado "
		FinSi
	FinSi
	
	
FinAlgoritmo
