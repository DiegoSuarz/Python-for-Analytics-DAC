## 1. Opciones de primer y segundo nivel

chat = {}

chat['comprar una linea'] = {'pre pago':{},'post pago':{}}
chat['comprar un equipo'] = {'liberado':{},'pre pago':{},'post pago':{}}
chat['internet hogar'] = {'moden movil':{},'moden hogar':{}}

chat

### Opciones de tercer nivel
chat['comprar una linea']['post pago'] = {'basico':29,'control':44,'plus':60}
chat['comprar una linea']['post pago']

chat['comprar una linea']['pre pago'] = {'super chip':5,'flex chip':0}
chat['comprar una linea']['pre pago']

chat['comprar un equipo']['liberado'] = {'Motorola':380,'Samsung':500,'Huawey':350}
chat['comprar un equipo']['liberado']

chat['comprar un equipo']['pre pago'] = {'Motorola':350,'Samsung':480,'Huawey':320}
chat['comprar un equipo']['pre pago']

chat['comprar un equipo']['post pago'] = {'Motorola':310,'Samsung':450,'Huawey':290}
chat['comprar un equipo']['post pago'] 

chat['internet hogar']['moden movil'] = {'basico':49,'estandar':69,'premiun':99}
chat['internet hogar']['moden movil']

chat['internet hogar']['moden hogar'] = {'basico':69,'estandar':99,'premiun':149}
chat['internet hogar']['moden hogar'] 

chat
chat.keys()

for x in chat.keys() :
  print(x)

## Navegando en el diccionario
mi_ops = chat.keys()
mi_ops

opc = list(chat.keys()) #convertir llaves en una lista
opc

##### PROGRAMA.
for i in range(0,len(chat)):
  print(chat[opc[i]])

opc = list(chat.keys())
opc

print("Bienvenido a la empresa CelTel")
print("\nIngrese el numero de la opcion\n")
for x in range(0,len(opc)):
  print(f"{x+1}.{opc[x]}")

mi_opcion = int(input("\n"))
mi_opcion -= 1

chat2 = chat[opc[mi_opcion]]
#fin del primero

opc2 = list(chat2.keys())
print("\nIngrese el numero de la opcion\n")
for x in range(0,len(opc2)):
  print(f"{x+1}.{opc2[x]}")

mi_opcion2 = int(input("\n"))
mi_opcion2 -= 1

chat3 = chat2[opc2[mi_opcion2]]
#fin del primero
opc3 = list(chat3.keys())

print("\nIngrese el numero de la opcion\n")
for x in range(0,len(opc3)):
  print(f"{x+1}.{opc3[x]}")

mi_opcion3 = int(input("\n"))
mi_opcion3 -= 1

print(f'El precio de {opc2[mi_opcion]} en {opc3[mi_opcion2]} es: {chat3[opc3[mi_opcion3]]} soles')




