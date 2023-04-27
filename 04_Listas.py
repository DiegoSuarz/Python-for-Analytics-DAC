###LISTAS
"""Las listas en Python son uno de los tipos o estructuras de datos más 
versátiles del lenguaje, ya que permiten almacenar un conjunto de datos.
Es decir, podemos guardar un ellas prácticamente lo que sea. Si vienes
de otros lenguajes de programacion, se podria decir que son similares a los 
arrays.
"""

###INDICES EN LISTAS
#Se trabaja de manera similar a los caracteres de texto
["VISUAL","2"*2,1,[0,1,2,3]]

Lenguajes = ['Python','Java','C','R','VBA']

Lenguajes[0]
Lenguajes[1]

Lenguajes[-1] #ultimo elemento

##AGREGAR ELEMENTOS:
Lenguajes = Lenguajes + ['DAX']
Lenguajes

Lenguajes += ['HTML','SQL']
Lenguajes

Lenguajes.append('PHP')
Lenguajes

##EXTRAER ELEMENTOS:
curso = Lenguajes[0]
curso

curso1 = Lenguajes[0:3] #extraer 3 elementos (se forma un lista)
curso1

c1,c2,c3 = Lenguajes[0:3]
c1
c2
c3

### INCLUSION:
#Se le puede preguntar a python si un elemento esta presente en la lista
'C' in Lenguajes
'stata' in Lenguajes

### EXCLUSIÓN:
#Podemos invertir el criterio anterior
'C' not in Lenguajes
'stata' not in Lenguajes

### DEFINIENDO LISTAS:
miLista = [] #definir el objeto miLista

miLista.append("textos")
miLista.append("numero")
miLista.append("booleano")
miLista

miLista.clear() #limpiar la lista
miLista

### CREAR UNA LISTA EQUIVALENTE
miLista1 = []

miLista1.append("for")
miLista1.append("while")
miLista1.append("if")
miLista1

miLista2 = miLista1 #todo cambio que se hace en ambas listas influyen en las 2
miLista1.append("switch")
miLista1.append("case")
miLista1.append("Break")

miLista2.append("do while")
miLista2.append("continue")

#ambos objetos tienen los mismo elementos ya que con equivalentes (hemos puesto un distinto nombre a un mismo objeto)
miLista1
miLista2

###CREAR UNA COPIA
miLista3 = miLista1.copy()

miLista1.append("define")
miLista1
miLista2
miLista3