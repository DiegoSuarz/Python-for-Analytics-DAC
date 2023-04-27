""" 
def suma(a,b):
    print(a + b)

suma(1,3)
 """
##########################################################
""" 
def doble(x):
    print(f'El doble de {x} es {2*x}')

doble(3)
 """ 
##########################################################
""" 
def raiz(y):
    print(f"La raiz de {y} es {y**0.5}")

#raiz(-25) #el resutado es un valor imaginario: 3.061616997868383e-16+5j
raiz(25)
 """
##########################################################
""" 
def raiz(y):
    if y < 0:
        print("El numero debe ser positivo")
    else:
        print(f"La raiz de {y} es {y**0.5}")
#raiz(-25) #el resutado es un valor imaginario: 3.061616997868383e-16+5j
raiz(5)
 """
##########################################################

""" def suma(a,b):
    if type(a) == int and type(b) == int:
        print(a + b)
    elif type(a) == str and type(b) == str:
        print(a + " " + b)
    elif type(a) == bool and type(b) == bool:
        print("Los datos son booleanos")
    else:
        print("Los elementos deben coincidir")

# suma(1,2)
# suma('b','c')
suma(True,True) """

##########################################################
""" 
def suma_exp(a,b):
    print(f'La suma de {a} + {b} es {a+b}')

suma_exp(3,5)
 """
##########################################################
### return:
# Para generar un contenido o resultado almacenable:
""" 
def suma_2(a,b):
    print(f'La suma de {a} + {b} es {a+b}')
    return a + b

resultado = suma_2(1,3)
print(f'El resultado es: {resultado}')
 """
##########################################################
""" 
def es_par(x):
    for i in range(1,x+1):
        print(f'Para {i} se  obtiene {i % 2 == 0}')

es_par(10)

 """
##########################################################
## MULTIPLES RESULTADOS
""" 
def mas_menos(x,y):
    x1 = x - y
    x2 = x + y
    return x1,x2

a,b = mas_menos(2,3)
a,b = mas_menos(13,2.5) #se transforma en una tupla

print(f'Los valores son a = {a} y b= {b}') 
 """
 ##########################################################
""" 
def mas_menos(pronostico, margen):
    li = pronostico - margen
    ls = pronostico + margen
    print(f'El estimado va desde {li} hasta {ls}\n')
    return li,ls

peor,mejor = mas_menos(30,7)
print(f'el peor valor es: {peor}, el mejor valor es: {mejor}')
 """
 ##########################################################
""" 
def calculadora(num):
    x1 = num ** 2
    x2 = num *- 20
    x3 = num % 2
    print(f'Al elevarlo al cuadrado es: {x1}\nSi lo multiplicamos por -20 es: {x2}\nEl residuo al dividirlo entre 2 es: {x3}')
    return x1,x2,x3

calculadora(5)
 """
##########################################################
## DECORADORES es un tipo de objetos
""" 
def decorador(funcion):
    def mi_funcion(y):
        print("Inicio del proceso") #paso1
        print(f"El argumento es de tipo {type(y)}") #paso2
        print(funcion(y)) #paso3
        print("Fin del proceso") #paso 4
    return mi_funcion

@decorador
def doble(x):
    return 2*x

@decorador
def mitad(x):
    return x/2

# doble(4)
mitad(8)
 """
##########################################################
""" 
def detalle(fun):
    def fun_detalle(a):
        print("Inicio del programa")
        print(f"El dato analizado es: {type(a)}")
        if type(a) == int:
            print(f'la mitad del numero es {a/2}')
        elif type(a) == str:
            print(f'El largo del texto es: {len(a)}')
        print(f'El resultado de la funcion es: {fun(a)}')
        print("Fin del programa")
    return fun_detalle

@detalle
def raiz(x):
    return x**0.5

@detalle
def saludo(x):
    return f'{x}'

#raiz(25)
saludo("Hola mundo")
 """
##########################################################
## GLOBAL Y RETURN
""" 
def cero():
    global a  #se toma el valor de a como fuera de la funcion
    a = 0
    print(a)
    return a

r = cero()
 """
""" 
def es_entero(x):
    y=int(x)
    if x-y !=0:
        #exite un exceso
        global exceso
        exceso = x - y
        print(f'Se idenfico un exceso de: {exceso}')
    mi_boll = x == y
    return mi_boll

# ev_11_8 = es_entero(11.8)
resp = es_entero(9)
 """
##########################################################
## FUNCIONES CON ARGUMENTOS VARIABLES:
# ENFOQUE TUPLA: 
""" 
def sumar(*ars): #ars hacer referencia a una tupla
    suma = 0
    for i in ars:
        suma += i
    print(suma)    
    return suma

sumar(1,3,5,6,7) # se le envian multiples valores a la funcion
 """
##########################################################
""" 
def sumar2(*ars):
    return sum(ars)

res = sumar2(1,3,6,4)
print(res)
 """
##########################################################
# ENFOQUE DICCIONARIO: 
""" 
def sumaMultiple(**kwargs):
    suma = 0
    print(kwargs)
    for llave,valor in kwargs.items():
        print(f'La llave {llave} es: {valor}')
        suma += valor
    return suma

sumaMultiple(x=5, y=7, z=9, m=8)
 """
##########################################################
# ENFOQUE MULTIPLE
""" 
def funcion(a,b,c,*args, **kwargs):
    print("a =",a)
    print("b =",b)
    print("c =",c)
    c=0
    for arg in args:
        print(f'indice {c} de la tupla es: {arg}')
        c += 1
    for llave, valor in kwargs.items():
        print(llave, "=", valor)

funcion(12,34,23,54,65,34,x=5,y=4,z=45,m=23)
 """
##########################################################
# ENFOQUE MULTIPLE
# FILTRO:
""" 
puntaje = [13,16,8,17,10]

def esAprobado(mi_lista):
    return mi_lista > 10

aprobados = []
for nota in puntaje:
    if esAprobado(nota):
        aprobados.append(nota)

print(aprobados)
 """
# Otro metodo usando la funcion filter
""" 
puntaje = [13,16,8,17,10]

def esAprobado(mi_lista):
    return mi_lista > 10

resp = list(filter(esAprobado,puntaje))
print(resp)
 """
##########################################################
## MAP:
""" 
puntaje = [13,16,8,17,10]
mitades = []

for nota in puntaje:
    mitades.append(nota/2)

print(mitades)
 """
#otro metodo usando la funcion MAP:
""" 
puntaje = [13,16,8,17,10]

def mitad(nota):
    return nota/2

resp = list(map(mitad,puntaje))
print(resp)
 """
##########################################################
# ESTRUCTURA DE DATOS SET(CONJUNTOS):
# definiciones:
""" 
lista1 = [1,3,5,7,9,13,15,18]
lista1

lista1 = set(lista1)
type(lista1)

lista2 = [2,3,4,5,4,6,8,10,11,16]
lista2

lista2 = set(lista2)
type(lista2)

#OPeradores entre conjuntos:
#UNION:
lista1.union(lista2) #unir conjuntos

#INTERSECCION
lista1.intersection(lista2) #elementos en comun

#DIFERENCIA:
lista1.difference(lista2) #elemntos estan presente en la lista1 que son diferentes que en la lista2
lista2.difference(lista1) #elemntos estan presente en la lista2 que son diferentes que en la lista1
 """
##########################################################
## OPERADOR TERNARIO:

# nota = 10
nota = 16
resp = "aprobado" if nota > 10 else "desaprobado"
print(resp)
