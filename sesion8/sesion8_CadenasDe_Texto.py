# Las comillas triples son las que se encargan de hacer
# Cadenas de texto largas sin modificar el formato del
# texto corto
cancion = "De tantas mujeres, chale, pues me saliste igualita"
"Ni pedo, pues ya ni que hacerle"
"Maldito cariño, era todo una mentira"
"Fuiste fugaz"


# textos largos ''' o """"


cancion1 = """De tantas mujeres, chale, pues me saliste igualita
Ni pedo, pues ya ni qué hacerle
Maldito cariño, era todo una mentira
Fuiste fugaz
Me eché otro whiskacho
Por amor hace rato que no bebía
Chale, ni pa qué les cuento
Bien sarra que se siente sin ti empezar el día
Y terminar
Qué tranquila se te ve
Y yo bien malilla por darte otra vez, uh-oh, oh
Bien, me saliste, pero bien infiel
Bonita y canija, vieras qué mal te ves, uh-oh, oh
Ay, mamá
Double P
Fuiste mi peor error del año
Cambiaste todo y la fuiste a cagar
Ando en carrito del año
Llego volando en jet particular
Con otra morra que no eres tú
Que está más fina y de más grande cu-
Dos margaritas por Malibú
Aquí anduvieras, pero andas de pu-
Qué tranquila se te ve
Y yo bien malilla por darte otra vez, uh-oh, oh
Bien, me saliste, pero bien infiel
Bonita y canija, vieras qué mal te ves, uh-oh, oh"""

## print(cancion1)

## computadora -> que variable queres imprimir?
## print() =>
# void -> no devuelve nada
# objeto -> devuelve un tipo de dato
#

# 3 realizar una wiki tambien puede darle doble clic documento y se les
## despliega el editor de texto

## MAYUSCULAS
## mutabilidad -> siempre debemos evitar transformar onjeto original
## clases -> estereotipo (como un molde)
## propiedades ->


## cancion es un espacio de memoria para string
# se va a llenar con el contenido de la cancionalteraar la accion upper
cancion1_Mayusculas = cancion1.upper()
## print(cancion1_Mayusculas)

# convertir en minusculas
# string.lower

cancion_minusculas = cancion1.lower()
## print(cancion_minusculas)

mensaje = "HolA kAce prOgRamAndO o k hAce"

mensaje_correcto = mensaje.capitalize()
## print(mensaje_correcto)

## Las flipantes aventuras de el gato con bolson magido y alfredo
titulo = "Las flipantes aventuras de el gato con bolson magido y alfredo"
titulo_correcto = titulo.title()
## print(titulo_correcto)

##  swapCase -> permite cambiar entre mayusculas y minusculas
swapCaseTitulo = titulo_correcto.swapcase()
print(swapCaseTitulo)
