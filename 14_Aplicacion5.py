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


#paso 1, ofrecer las primeras opeciones
opc = list(chat.keys())
print("Bienvenido a la empresa CelTel")
print("\nIngrese el numero de la opcion\n")
for x in range(0,len(opc)):
  print(f'{x+1}.{opc[x]}')
print("")
#paso 2 recibir la opcion de primer nivel
x = int(input(""))

#paso 3 ofrecer las opciones de la primera eleccion
chat_2 = chat[opc[x-1]]
opc2 = list(chat_2.keys())
print("\nIngrese el numero de la opcion\n")
for x in range(0,len(opc2)):
  print(f'{x+1}.{opc2[x]}')
print("")
#paso 4 recibir la opcion de segundo nivel
x2 = int(input(""))

#paso 5 ofrecer las opciones de tercer nivel
chat_3 = chat_2[opc2[x2-1]]
opc3 = list(chat_3.keys())
print("\nIngrese el numero de la opcion\n")
for x in range(0,len(opc3)):
  print(f'{x+1}.{opc3[x]}')
print("")
#paso 6 recibir la opcion de tercer nivel
x3 = int(input(""))
print("")
print(f'El precio de {opc2[x2-1]} en {opc3[x3-1]} es: {chat_3[opc3[x3-1]]} soles')