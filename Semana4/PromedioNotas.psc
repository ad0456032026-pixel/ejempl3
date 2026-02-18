Algoritmo PromedioNotas
	Definir Numero1, Numero2, Numero3, promedio Como real 
	// solicitar al usuario
	// ingresar tres notas 
	// y mostrar el promedio de ellas
	Escribir "Ingrese tres calificaciones: "
	Leer Numero1, Numero2, Numero3
	
	Si Numero1 >= 0 y Numero2 >= 0 y Numero3 >= 0 Entonces
		promedio = (Numero1 + Numero2 + Numero3) / 3
		Escribir "El promedio es: " , promedio 
	SiNo
		Escribir "Error: las calificaciones no pueden ser negativas. "
	FinSi
FinAlgoritmo
