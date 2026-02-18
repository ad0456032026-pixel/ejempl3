Algoritmo SumarTres
	// solicitar al usuario
	// que ingrese tres numeros enteros
	// y mostrar la suma de todos 
	Definir Numero1, Numero2, Numero3, suma Como Real 
	Escribir "Ingrese tres numeros para sumarlos: "
	Leer Numero1, Numero2, Numero3
	
	// hacemos la suma sin restricciones
	
	suma = Numero1 + Numero2 + Numero3
	
	// usamos el "Si" para clasificar el resultado
	
	Si suma > 0 Entonces
		
		Escribir "La suma total es POSITIVA: " , suma
	sino 
		Escribir "La suma total es CERO o NEGATIVA: " , suma
	FinSi
FinAlgoritmo
