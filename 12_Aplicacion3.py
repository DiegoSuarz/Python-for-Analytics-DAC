######## Ejercicios de complemento:

"""
datos_1 = {'nombre':'sergio', 'apellido':'diaz', 'pwd' : 'dth4', 'telefono' : '1234'}
datos_2 = {'nombre':'luis', 'apellido':'rios', 'pwd' : 'kjd9', 'edad' : '25'}
datos_3 = {'nombre':'noemi', 'apellido':'osco', 'pwd' : 'ikl7', 'carrera' : 'economia'}

base = {'sdiaz' : datos_1, 'lrios' : datos_2, 'nosco' : datos_3}


base['lrios']
base['sdiaz']
base['nosco']
base['lrios']['pwd']
base
base['lrios']['nombre']
base['sdiaz']['nombre']
base['nosco']['nombre']

base['lrios'].items()

user = input('Dimer tu usuario:\n')
while user not in base.keys():
    print('¡Usuario no registrado!')
    user = input('Por favor ingrese un usuario existente:\n')
#una vez que se garantiza que el usuario exite en la base de datos:
pwd = input("Dime tu contraseña:\n")
while pwd != base[user]['pwd']:
    pwd = input(f'Contraseña incorrecta\nIngrese la contraseña de {user}\n')
name = base[user]['nombre']
print(f'\nBienvenido {name}\nTenemos registrados tus siguientes datos:\n')

for key,val in base[user].items():
    print(f'Tu {key} es {val}')

 """
###################################
# AGREGANDO NUEVOS USUARIOS:
""" 
datos_1 = {'nombre':'sergio', 'apellido':'diaz', 'pwd' : 'dth4', 'telefono' : '1234'}
datos_2 = {'nombre':'luis', 'apellido':'rios', 'pwd' : 'kjd9', 'edad' : '25'}
datos_3 = {'nombre':'noemi', 'apellido':'osco', 'pwd' : 'ikl7', 'carrera' : 'economia'}

base = {'sdiaz' : datos_1, 'lrios' : datos_2, 'nosco' : datos_3}


nuevoNombre = input('¿Cual es tu nombre?\n')
nuevoApellido = input('¿Cual es tu apellido?\n')
nuevoUsuario = nuevoNombre[0] + nuevoApellido
nuevoUsuario
print(f'Estimado {nuevoNombre}, tu nuevo usuario es: {nuevoUsuario}')
nuevoPwd = input('¿Escribe tu contraseña?:\n')
nuevoDict = {'nombre': nuevoNombre, 'apellido': nuevoApellido, 'pwd':nuevoPwd}

resp = input('¿Quieres agregar un dato adicional?\n')
while resp == 'si':
    new_key = input('¿Que dato quieres registrar?:\n')
    new_val = input(f'¿Cual es tu {new_key}?\n')
    nuevoDict[new_key] = new_val
    print(f'Se registro tu {new_key} como {new_val}\n')
    resp = input('¿Quieres agregar un dato adicional?\n')

base[nuevoUsuario] = nuevoDict
base[nuevoUsuario] 
print(f'Se registraron sus datos en la cuenta de usuario {nuevoUsuario}')
 """
###################################
# AGREGANDO NUEVOS USUARIOS:


datos_1 = {'nombre':'sergio', 'apellido':'diaz', 'pwd' : 'dth4', 'telefono' : '1234'}
datos_2 = {'nombre':'luis', 'apellido':'rios', 'pwd' : 'kjd9', 'edad' : '25'}
datos_3 = {'nombre':'noemi', 'apellido':'osco', 'pwd' : 'ikl7', 'carrera' : 'economia'}

base = {'sdiaz' : datos_1, 'lrios' : datos_2, 'nosco' : datos_3}

mi_nombre = input("¿Cual es tu nombre?\n")
mi_app = input("\n¿Cual es tu apellido?\n")

new_user = mi_nombre[0] + mi_app
cont_name = 2

while new_user in base.keys():
  new_user = mi_nombre[0:cont_name] + mi_app
  cont_name += 1

print(f'\nEstimado {mi_nombre} se creo su usuario: {new_user}')
mi_pwd = input("\nEscriba su contraseña\n")
my_dic = {'nombre': mi_nombre, 'apellido': mi_app,'pwd': mi_pwd}
agregar = input("\n¿Desea agregar un dato adicional?[si,no]\n")
while agregar not in ['si','no']:
  agregar = input("\nPor favor conteste con si o no")

while agregar=="si":
    mi_dato_nombre = input("\n¿Que dato desea agregar?\n")
    mi_dato_valor = input(f"\n¿Cual es su {mi_dato_nombre}?\n")
    my_dic[mi_dato_nombre] = mi_dato_valor
    agregar = input("\n¿Desea agregar un dato adicional?[si,no]: ")
    while agregar not in ['si','no']:
        agregar = input("\nPor favor conteste con si o no\n")

base[new_user] = my_dic
my_dic
print(f"\nSe registraron sus datos en la cuenta de usuario {new_user}")
