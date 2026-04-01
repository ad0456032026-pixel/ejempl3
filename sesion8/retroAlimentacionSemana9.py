serie = "Fullmetal alchemist"

### cada variable tiene un espacio de memoria asignado

## cuando una variable cambia => se piierde la inmutabilidad
## POO
## polimorfismo -> es el cambio de acciones sinque se rompa el codigo
## abstracciones ->
##       Tasa de cafe
##       cafe coscafe
##       azucar
##       agua
##       otros ingredientes
##  un objeto es el que toma un modelo y este modelo  le da funciones y utiliza sus propiedades

## Leon -
## tiene ojos (propiedades)
## tiene boca
## esta guapo
#############
## corre      (Funciones)
## salta

## Clases
## Estructura de datos.


## un arreglo es una variable que adentro tiene otra variable
## Listaas.
## Arrays. -> se inicia a contar desde el cero (0)
## tuplas.
## indices.


# -----------------------------------------------------------------
def saludo(nombres):
    print(nombres)


# saludo(serie) las funciones siempre van a tener ()
# -----------------------------------------------------------------
## las funciones tienen un espacio
## Scope es donde reciden las variables

## Colocar el nombre de la serie como titulo
fmaTemu = serie.title()
## saludo(serie)
## saludo(fmaTemu)
fmaMayusculas = serie.upper()
saludo(fmaMayusculas)
## deprograccion lineal

FullmetalCapitalizer = fmaMayusculas.swapcase().title()
## cuand0 ordenamos funciones se indicaa que la salida de la funcion actual
## es la entrada de la siguiente funcion
saludo(FullmetalCapitalizer)

## compara cadenas de texto

nombre = "Ever Alfredo Osorto"
password = 123456789

nombre = input("Ingresa tu nombre: ")

if nombre == "Ever Alfredo Osorto":
    password = input("Ingresa tu password: ")
    if password == "1234":  # aquí puedes poner la contraseña correcta
        print("Welcome bro!")
    else:
        print("Contraseña incorrecta")
else:
    print("No eres tú bro")

## comparar cadenas de texto
comparar1 = "Ever "
comparar2 = "Ever"

variableTemporal = comparar1.casefold()
comparar = comparar1.casefold() == comparar2.casefold()
# print(comparar)
## casefold nos dara true unicamente si los elementos son identicos sino nos indicara un false

## para ferificar si es un numero o un caracter vamos a utilizar isalfa()
clasicas2005 = "Gasolina"
compararisAlpha = clasicas2005.isalpha()
# print(compararisAlpha, 2005)
##isalpha nos dara un true si el string que se esta enviando tiene solo letras

## si lo que quiero es que sea solo numero

letraCancion = "lo que paso paso, entre tu y yo."  # no tengo numero
decada = "10"

ejemplo = letraCancion.isalnum()
print(ejemplo)
ejemplo = decada.isalnum()
## isalnum verifica si la cadena de texto solo tiene numeros, si es asi nos dara true
## si tiene un solo espacio nos dara un false

## verificar que solo sean digitos
comprobarDecadas = decada.isdigit()
print(comprobarDecadas)

## si la cacddnqa de textgo tiene numeros
SiTienenNumero = "2026"
## si este texto tiene numero -> true
## isnumeric -> es un espacio en la memoria
## isnumeric() -> dentro de la funcion
respuesta = SiTienenNumero.isnumeric()
print(respuesta)

## isumeric como numeros que van a estar ejecutandose desde una
## cadena de texto

isLowerCase1 = " Ella se fue, me abandono y me destrozo mi corazon"
minusculas = isLowerCase1.islower()
## isLowerCase()
## isLowerCase.isLower()
## true o false
print("solo minusculas:", minusculas)

## 3 minutos

isnombre_minusculas = "Cristiano Leo son"
nombre_minusculas = isnombre_minusculas.islower()
print("solo minusculas:", nombre_minusculas)

fraseIconica = "Desoltala Erika"
respuesta = fraseIconica.isupper()
print(respuesta)

## tener un contenido -> entrada a la funcion que inicie con el punto .
respuesta = fraseIconica.upper().isupper()
## esta funcion la vamos a encadenar con la otra >:)
print(respuesta)

respuesta = fraseIconica.title().istitle()
print(fraseIconica, respuesta)
## cuando una funcion retorna algo ( tipo de datos)
## String -> un espacio de memoria difente al de un espacio numerico
## integer
## float
## Decimal
## Boolean

# String -> E v e r -> una lista o array
# varianle :
# tiene un tipo -> indice
#  nombre sea unico -> indice
# no puede indicar con variables
# va a tomar siempre el calor de la ultima modificacion
print(serie)
serie = "El chavo de el 8"
print(serie)

controlarEspacio = serie.isspace()
print(controlarEspacio)
## islower
# isupper
# isspace
# isalum
# isalpha

## Metodos de busqueda
tema = "En el bosque de china la chinita se perdio  "
#  E n e l b o s q u  e  d  e  c  h  i  n  a  l  a  c  h  i  n  i  t  a  s  e  p  e  r  d  i  o
#  1 2 3 4 5 6 7 8 9 10  11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
## siemprem parte desde el 0 al ultimo numero
## si indicamos algo que no esta en el  string nos va a indicar -1
temaf = tema.find("china")
print(temaf)

## desde la derecha vamos a tomaar en ceunta lo siguuiente rfind()
temaf = tema.upper().rfind("BOSQUE")
print(temaf)

poema = """ Ella amará a otro hombre.
Yo voy lejos, andando hacia el olvido.
Y puede suceder que alguien me nombre,
pero ella fingirá no haber oído.

Ella amará a otro hombre:
el tiempo pasa y el amor finaliza,
y es natural que lo que fue una brasa
acabe convirtiéndose en ceniza."""

contador = poema.count("i")
contador = poema.startswith("Ella")
contador = poema.endswith("ceniza.")
# print(contador)

poemaModificado = poema.replace(" Ella ", " Lupita ").replace(" amará ", " floow ")
print(poemaModificado)
