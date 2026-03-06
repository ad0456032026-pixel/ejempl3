Algoritmo Ejercicio7ProductoCociente
	
	Definir primerNumero, segundoNumero, resultadoProducto, resultadoCociente Como Real
	
	Escribir "Calculadora (producto y cociente) "
    Escribir "Ingrese el primer número: "
    Leer primerNumero
    
    Escribir "Ingrese el segundo número: "
    Leer segundoNumero
	
	resultadoProducto <- primerNumero * segundoNumero
    Escribir "El producto de ambos numeros es: ", resultadoProducto
	
	Si segundoNumero <> 0 Entonces
        resultadoCociente <- primerNumero / segundoNumero
        Escribir "El cociente del primero entre el segundo es: ", resultadoCociente
    SiNo
        Escribir "Error matemático: ¡No se puede dividir entre cero!"
	Finsi
FinAlgoritmo
