Algoritmo Ejemplo2
	Definir cajero, cuentaDeAhorro,numeroCuenta, CanidadSaliente, Saldo, preguntar como entero
	cuentaDeAhorro = 1000
	numeroCuenta = 12345
	
	Escribir " bienvenido" 
	Escribir " Actividad que desea realizar"
	Escribir " 1 para consultar"
	Escribir " 2 para extraer dinero de la cuenta de ahorro"
	
	Escribir " Escriba el numero de cuenta a operar"
	Leer preguntar // yo no quiero ser un uno mejor busco otra chamba
	
	si preguntar == 1
		Escribir " Escriba el numero de cuenta a operar"
		Leer preguntar // es valor del numero de cuenta 
		
		si preguntar == numeroCuenta
			Escribir " Su saldo es " , cuentaDeAhorro
		FinSi
	FinSi
	
	
	si preguntar == 2
		Escribir " Escriba el numero de cuenta a operar"
		Leer preguntar // es valor del numero de cuenta 
		
		si preguntar == numeroCuenta
			Escribir " Escriba el monto a extraer " 
			leer preguntar // es la cantidad a extraer
			
			si preguntar <= cuentaDeAhorro 
				saldo = cuentaDeAhorro - preguntar
				Escribir "Procesando"
				Escribir  "su saldo actual es de " , saldo
			FinSi
		FinSi
	FinSi
	
	
	
	
	
	// or o puedes llevar
	// panes con cafe o chocolate
	
	// and puedes llevar carne y jamon 
	
	// not mejor no
	
	// == si es igual 
	// 
	
	
	
	
	// no pueden comenzar con 
	// numeros
	// signos a menos que sea _
	// no deben llevar espacio
	// Si es una clase siempre inicia con Mayusculas 
	// es evitar el codigo spaguetti 
FinAlgoritmo
