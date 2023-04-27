#### Funciones Lambda:
""" 
def f_polinomio(num):
    return (num**2 + 2*num)

res = f_polinomio(2)
print(res)

f_polinomio2 = lambda num: num**2 + 2*num
res1 = f_polinomio2(3)
print(res1)

#ENFOQUE TUPLA:
## con 2 variables.
f_polinomio3 = lambda x,y: x**2 +2*x + y
res2 = f_polinomio(4)
print(res2)

## sin declarar la funcion lambda
(lambda x,y: x**2 + 2*x + y)(1,2)
 """
########################################################
#### FUNCION LAMBDA COMO FILTRO:
""" 
lista = [1,2,3,4,5]
lista2 = list(filter(lambda x: x%2 == 0, lista)) #filtra los numeros pares
print(lista)
print(lista2)
 """
########################################################
#### DATATIME:

import datetime as dt

dt.datetime(2023,4,22,11,59)
dt.datetime(2023,3,27)

dt.datetime(2023,4,22,11,59).strftime("%Y-%m-%d-%H-%M")
dt.datetime(2022,2,20).strftime("%Y-%m-%d")

dt.datetime.now()
dt.datetime.now().strftime("%Y-%m-%d-%H-%M")

a = dt.datetime.now()
a.strftime("%Y-%m-%d-%H-%M")
print(a)

#incremento en el tiempo:
dt.timedelta() 

b = dt.timedelta(hours =- 5)
print(b)

c = a + b
print(c)

##############################
fecha_inicio = dt.datetime(2023,2,28,21,26)
fecha_fin = dt.datetime(2023,3,17,22,0)

delta_d = fecha_fin - fecha_inicio
print(delta_d)





