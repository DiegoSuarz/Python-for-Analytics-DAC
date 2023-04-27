## Esctructura de control condicional IF:
## IF
""" nota = int(input("¿C8ual fue tu nota?\n"))

if nota > 12:
    print("Aprobaste")

if nota <= 12:
    print("No aprobaste") """

## ELSE:
#Complementa IF par poder indicar la sentencia a ejecutar en case no se cumpla el criterio

""" nota = int(input("¿C8ual fue tu nota?\n"))

if nota > 12:
    print("Aprobaste") #solo se ejecuta si es verdadero

else:
    print("No aprobaste") """

## ELIF
# En caso no se cumpla el criterio principal todavia se puede brindar una orden especifica para una situación especifica.

nota = int(input("¿Cual fue tu nota?\n"))

if nota > 12:
    print("Aprobaste")

elif nota == 12:
    print("Requiere recuperacion")

elif nota <= 5:
    print("Retiro de curso")

elif nota == 0: #no se ejecuta ya primero se ejecuta la sentencia nota<=5 ya que se ejecuta antes en tiempo de ejecución
    print("Se requiere asesoria")
else:
    print("No aprobaste")