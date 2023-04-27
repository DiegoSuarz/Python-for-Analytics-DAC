####DICCIONARIOS:

###DEFINICION:
""" 
dias = dict() #primera opcion
semanas = {} #segunda forma

dias = {'01':'Lunes',
        '02':'Martes',
        '03':'Miercoles',
        '04':'Jueves',
        '05':'Viernes',
        '06':'Sabado',
        '07':'Domingo',}
dias

## EXPLORANDO:
len(dias) #muestra el numero de elementos del dic

dias.items() #muestra las llaves y los valores del dic

dias.keys() #muestra las claves

dias.values() #muestra los valores de los elementos del dic

dias.get('01') #muestra el valor de una llaves en especifico
dias['07'] #otra forma de acceder al valor de una llave especifica
 """
## AGREGARNDO VALORES:
""" 
numeros = {}
numeros ={'1':'Uno','2':'Dos','3':'Tres','4':'Cuatro'}
numeros['5'] = "Cinco"
numeros

key = input("Dime un numero:\n")
print(numeros[key])

'1' in numeros.keys()

'Uno' in numeros.values()
 """
####################################
### UNIENDO LISTAS
prog = ['R' , 'DAX', 'PYTHON', 'SQL']
cal = [9,5,7,6]
#uniendo listas para formar diccionarios:
""" 
skills = {i:j for (i,j) in zip(prog,cal)}
skills
 """
## otro metodo:
""" 
skills1 = {}
for i in range(0,len(cal)):
    skills1[prog[i]] = cal[i]
print(skills1)

## EN BUCLE FOR:
print(skills1.items()) #mostrar los items como una tupla

for key, valor in skills1.items():
    print(f'tu nivel de {key} es {valor}')
 """
## ANIDADO DE DICCIONARIOS
skills2 = {'R': 9, 'DAX': 5, 'PYTHON': 7, 'SQL': 6}
skills2['R']

skills2['R'] = {'RSTUDIO':9,'R':3,'RCLOUD':5}
skills2
