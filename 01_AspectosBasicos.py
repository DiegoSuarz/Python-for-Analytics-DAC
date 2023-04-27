
##########
edad = input("Ingrese Edad:") ##la funcion input siempre recibe el dato de entrada como un string
edad = int(edad) #se requiere convertir de string a tipo de dato que se desea

nombre = input("Ingrese Nombre: ")
apellido = input("Ingrese apellido: ")
carrera = input("Ingrese carrera: ")
print(f'Hola {nombre} {apellido}')
print(f'Usted tiene {edad} años')
print(f'Se encuentra estudiando la carrera de {carrera}')
print("gracias por su visita.")