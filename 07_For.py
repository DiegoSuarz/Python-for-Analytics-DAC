#### ESTRUCUTURAS DE CONTROL REPETITIVAS:

### FOR
""" 
 Es una estructura que permite definir un codigo a ejecutarse de manera
repetitiva con una argumento cambiante. En el siguiente ejemplo se aplica 
sobre una lista y el valor cambiante X es cada una de los elementos de 
esta lista """

""" 
dias_sem = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']

dias_sem[0]
dias_sem[1]

orden = 0
for dia in dias_sem: #recorre cada elementos de la lista dias_sem
    orden += 1
    print(f'El día {dia} es el N°{orden} de la semana')
    

cont = 0
for i in dias_sem:
    cont += 1
    print(f'Iteración N°{cont} --> {i}') #el indice es la posicion - 1
 """

### FUNCION Range() 
""" La funcion range nos permite crear un rango de numeros, la siguiente sentencia genera
un rango del 1 al 10 en el objeto ran_10. Si consultamos por este objeto tendremos como
resultado su rango definicion como rango """

""" 
ran_10 = range(1,10)  #iteracion 1 a 9 (n-1)
ran_10

for posicion in range(1,10):  #iteracion 1 a 9 (n-1)
    print(posicion)

for posicion in range(-5,5):    #iteraccion -5 a 4
    print(posicion)

for posicion in range(-5,5,2):    #iteraccion -5 a 4, saltando 2 posiciones
    print(posicion)
    
"""

## Break
# Rompe la continuidad del bucle:
""" 
for i in range(1,8):
    print(f' i vale {i}')

    if i == 4:
        print("Se ejecuta break")
        print("Fin del programa")
        break
    print(f'Fin de la iteracion {i}')
 """

#####
""" 
for i in range(1,8):
    print(f'Inicio de la iteración {i}')
    print(f' i vale: {i}')
    if i == 4:
        print(f'Fin de la iteración {i}\n')
        break
 """

## Continue:
# Fuerza la continuidad del bucle obviando la lienas de codigo que corresponden a la iteracion:

for i in range(1,8):
    print(f'Inicio de la iteración {i}')
    print(f' i vale: {i}')
    if i == 4:
        print(f'Se ejecuta continue \n')
        continue
    print(f'Fin de la iteración {i}\n')