#### Estructura de control repetitiva WHILE:
#Ejecuta una cantidad indefinida de repeticiones hasta que se cumpla un criterio

""" 
a = input("¿Quien tiene la razon, tu o yo? ")
while a == 'yo':
    a = input("No es cierto\n¿Quien tiene la razon, tu o yo?\n ")
print("Ya vez yo tenia la razon")
 """
###########

""" i = 0
while i < 10:
    print(i)
    i = i + 1
 """

##########
""" 
texto = input("Hola, por favor saludame ")
while texto != "hola":
    texto = input("Te pedi que me saludes\nPor favor dime hola ")
 """

 ##########
""" 
cont = 1
x = 30
while x < 50:
    print(f'Iteracion {cont}: x vale {x}')
    x = x + 5
    cont = cont + 1
 """
##########
""" 
resp = input("¿Cuanto es 2 + 2?\n")
while resp != '4':
    resp = input(f'\n!Incorrecto!\n2+2 no es: {resp}\nIntentalo otra vez:\n')
print("felicidades")
 """
##########
""" 
resp = input("¿Cuanto es 2 + 2?\n")
cont = 1
while resp != '4':
    resp = input(f'\n!Incorrecto!\n2+2 no es: {resp}\nIntentalo otra vez:\n')
    cont = cont + 1
print(f"\nfelicidades\nLo lograste en {cont} intentos!")
 """
#########
# "No".lower() not in ["si","no"]
#########
""" 
resp = input("¿Esta lloviendo?\n")
resp = resp.lower()
while resp not in ['si','no']:
    resp = input("¿Esta lloviendo?, por favor dime si o no\n")
    resp = resp.lower()
print("gracias")
 """
#########
#con 3 intentos
""" 
resp = input("¿Cuanto es 2 + 2?\n")
cont = 1
while resp != '4':
    if cont == 4:
        resp = input(f'\n!Incorrecto!\nEs tu ultimo intento, piensalo\n2 + 2 no es: {resp}\nIntentalo otra vez:\n')
        cont = cont + 1
        break
    resp = input(f'\n!Incorrecto!\n2+2 no es: {resp}\nIntentalo otra vez:\n')
    cont = cont + 1

if resp == '4':
    print(f"\nfelicidades\nLo lograste en {cont} intentos!")
else:
    print("Game over")
 """
###############
# Caso de aplicacion

cursos = []
niveles = []

n_cursos = int(input("¿Cuantos lenguajes de programación conoces?\n"))

for i in range(1,n_cursos+1):
    curso = input(f'\n¿Cual es tu lenguaje N°{i}? \n')
    while curso in cursos:
        curso = input(f"Ya me difiste {curso}\nDebes decirme otro lenguaje\n¿Cual es tu lenguaje N°{i}")
    cursos.append(curso)

    nivel = int(input(f"¿Cual es tu nivel en  {curso} del 1 al 10?\n"))
    while nivel not in range(1,11):
        nivel  = int(input(f"No es aceptado {nivel}\n¿Cual es tu nivel en {curso} del 1 al 10?\n"))
    niveles.append(nivel)

print("")
for i in range(0,n_cursos):
    print(f'Lenguaje N°{i+1} {cursos[i]}')
    print("|"*(niveles[i]*10))
    print("")



