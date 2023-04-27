
### UNION DE CADENAS

calle = "San Luis"
numero = "123 A"

calle + "." + numero 

### REPETICION DE TEXTO:
#La multiplicación de un texto es la repeticion continua
nombre = "Diego"

"luis"*3

print(nombre*3)

print('ja'*10)

print((nombre+" ")*3)

print((nombre + ', ')*3 + nombre)

#imprimiendo repeticiones:
texto = input("Ingrese un texto a repetir: ")     
repeticion = int(input("¿Cuantas veces quiere repetir este texto? "))
print((texto+", ") * (repeticion-1) + texto)


### Extension de texto
#Para saber cuantos caracteres tiene una cadena se emplea la funcion len()
apellido = "Suarez"
len("Diego")
len(apellido)

###Ubicacion de caracteres
#Cada elemento de una cadena de texto de tamaño N, esta representada por un indice de 0 a (N-1)
escuela = "UNMSM"
len(escuela)

escuela[0] #primer elemento del string
escuela[1]
escuela[2]
escuela[3]
escuela[4] #ultimo elemento del string

escuela[-1] #ultimo elemento del string
escuela[-2] 
escuela[-3]
escuela[-4]
escuela[-5] #primer elemento

###Secuencias:
#Podemos definir secuencias numericas que nos permitan ubicar indices
#textuasles, el ultimo elemento se excluye del indice.
#La siguiente cadena se conforma desde el indice 0(el primero) hasta
#el indice 2(tercer caracter)

trabajo="Ingeniero"

trabajo[0:3] #extrae los primero 3 elementos del string
#python considera los indices: 0,1,2 y el indice 3 no es tomado en cuenta [0,3>

"""Tambien podemos definir una secuencia de salto en el tercer elemento, sigregamas
un tercer elemento 1, la secuencia sera la misma"""

posicion = "123456789"

posicion[0:5:2] #de la posicion 0 al 5(-1) haciendo un salido de 2 elemento
posicion[0:5:1] #de la posicion 0 al 5(-1) haciendo un salido de 1 elemento 
posicion[0::2] #imprime todos los caracteres desde la poscion 0 haciendo un salto de 2 elemento

#####FUNCIONES TEXTUALES:
palabra = "Mensaje"

palabra.find('e') #te permite saber en que indice se encuentra un letra determina  en un string
palabra.find('j')
palabra.find('aje') #a partir de la posicion 4 se encuentra la palabra a buscar

palabra2 = "MensajeMensaje"
palabra2.find("aje") #siempre busca la primera ubicacion donde se encuentra la palabra a buscar

#poner la pimera palabra en mayuscula:
nombre1 = "diego suarez"
nombre1.capitalize() #pone mayuscula solo al primer elemento del texto
nombre1[0].upper() + nombre1[1:] #otro metodo

#title:
nombre2 = "diego suarez "
nombre2.title() #pone mayuscula al comienzo de todos las palabras del texto

#Todo a minuscula:
nombre3 = "Sergio Rosa"
nombre3.lower()

#Todo a mayuscula
nombre4 = "Denis Ayala"
nombre4.upper()

### SEPARADOR DE TEXTO (join) (unir texto)
"""Se coloca el primer elemento en medio de cada elemento del segundo
objeto, generando un texto nuevo"""

" y ".join(["texto 1","texto 2", "texto 3"])
", ".join(["Juan","Luis","Maria"])

### SEPARADOR DE TEXTO (split) (separar textos)
"Python, Java, C, R, VBA".split(", ") #convierte un string a una lista mendiante un delimitador
