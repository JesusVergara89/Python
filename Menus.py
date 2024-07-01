from tkinter import *
from tkinter import messagebox

root = Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Jesus", "Procesador de texto 2024")
def salirAplicacion():
    value = messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
    if value == "yes":
       root.destroy() 

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion = Menu(barraMenu)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")
archivoEdicion.add_command(label="Cortar")

archivoHerramientas = Menu(barraMenu)

archivoAyudas = Menu(barraMenu)
archivoAyudas.add_command(label="Licencia")
archivoAyudas.add_command(label="Acerca de", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyudas)


root.mainloop()