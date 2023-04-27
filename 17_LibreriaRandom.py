
#######################################################
#RANDOM::

import random as r

r.randint(0,100)

lista1 = []
for i in range(0,10):
    lista1.append(r.randint(0,100))
print(lista1)

lista2 = r.sample(lista1,5) #extraer 5 numeros aleatorios de la lista1
print(lista2)


empleados = ['JUAN','LUIS','FRANCISCO','TERESA','EMILIA','CARLOTA']
muestraAleatoria = r.sample(empleados,2)
print(muestraAleatoria)