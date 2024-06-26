from io import open

archivo_externo = open("archivo.txt", "w")

frase=input("Escribe una frase: ")

archivo_externo.write(frase)

archivo_externo= open("archivo.txt", "r")

texto = archivo_externo.read()

archivo_externo.close()

print(texto)





