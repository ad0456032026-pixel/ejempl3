Algoritmo Cuadrado
	// solicitar al usuario
	// que ingrese un numero
	// y mostrar su potencia al cuadrado
	Definir Numero1, resultado Como Real
	
	Escribir "Ingrese un numero para potenciarlo al cuadrado: "
	Leer Numero1
	Si Numero1 <> 0 Entonces
		resultado = Numero1 ^ 2
		Escribir  "El cuadrado de " , Numero1, " es: " , resultado
	SiNo
		Escribir "Error, cero al cuadrado seguira siendo cero. "
		
	FinSi
	
FinAlgoritmo
