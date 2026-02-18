Algoritmo VentaTienda
	// solicitar al usuario 
	// el precio de el producto
	// y la cantidad comprada
	// para mostrar el total a pagar
	Definir precio, cantidad, total Como Real
	
	Escribir "Ingrese el precio de el producto: "
	Leer precio
	
	Escribir "Ingrese la cantidad comprada: "
	Leer cantidad
	
	Si precio > 0 y cantidad > 0 Entonces
		total = precio * cantidad
		Escribir "El total a pagar es $" , total
	SiNo
		Escribir "Error: el precio o la cantidad deben ser mayores a cero"
	FinSi
	
FinAlgoritmo
