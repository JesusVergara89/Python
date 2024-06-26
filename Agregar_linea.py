from io import open

archivo_externo = open("archivo.txt", "a")

archivo_externo.write("\n\n Asegúrate de estar usando el entorno de Python correcto. Si estás utilizando un entorno virtual (virtualenv, conda, etc.), asegúrate de activarlo antes de ejecutar tu código:")

archivo_externo.close()