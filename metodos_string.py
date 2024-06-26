Nombre_usuario=input("introducuir nombre: ")

array_name = Nombre_usuario.split("@")

if len(array_name) > 1:
    print("ES es un nombre de correo válido")
else:
    print("NO es un nombre de correo válido")


print(array_name)