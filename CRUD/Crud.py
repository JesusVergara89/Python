from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

root.title("CRUD with python")
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#----------frames----------------------------------------

input_frame=Frame(root)
input_frame.pack()

btn_frame=Frame(root)
btn_frame.pack()

#---------------------------------------------------------

#----------labels----------------------------------------

idLabel = Label(input_frame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(input_frame, text="Nombre:")
nombreLabel.grid(row=1, column=0, padx=10, pady=10)

passLabel = Label(input_frame, text="Password:")
passLabel.grid(row=2, column=0,sticky="e", padx=10, pady=10)

apellidoLabel = Label(input_frame, text="Apellido:")
apellidoLabel.grid(row=3, column=0,sticky="e", padx=10, pady=10)

direccionLabel = Label(input_frame, text="Dirección:")
direccionLabel.grid(row=4, column=0,sticky="e", padx=10, pady=10)

comentariosLabel = Label(input_frame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0,sticky="e", padx=10, pady=10)
#---------------------------------------------------------

#----------inputs----------------------------------------

cuadroID = Entry(input_frame)
cuadroID.grid(row=0, column=1, padx=10,pady=10)

cuadroNombre = Entry(input_frame)
cuadroNombre.grid(row=1, column=1, padx=10,pady=10)

cuadroContrasena = Entry(input_frame)
cuadroContrasena.grid(row=2, column=1, padx=10,pady=10)
cuadroContrasena.config(show="*")

cuadroApellido = Entry(input_frame)
cuadroApellido.grid(row=3, column=1, padx=10,pady=10)

cuadroDireccion = Entry(input_frame)
cuadroDireccion.grid(row=4, column=1, padx=10,pady=10)

cuadroTexto = Text(input_frame, width=27, height=5)
cuadroTexto.grid(row=5, column=1, padx=10,pady=10)
scrollvert=Scrollbar(input_frame, command=cuadroTexto.yview)
scrollvert.grid(row=5,column=2, sticky="nsew")

cuadroTexto.config(yscrollcommand=scrollvert.set)

#---------------------------------------------------------

#----------Btns----------------------------------------
btnCrear = Button(btn_frame, text="Create")
btnCrear.grid(row=1, column=0, sticky="e", padx=10,pady=10)

btnLeer = Button(btn_frame, text="Read")
btnLeer.grid(row=1, column=1, sticky="e", padx=10,pady=10)

btnActualizar = Button(btn_frame, text="Update")
btnActualizar.grid(row=1, column=2, sticky="e", padx=10,pady=10)

btnEliminar = Button(btn_frame, text="Delete")
btnEliminar.grid(row=1, column=3, sticky="e", padx=10,pady=10)
#---------------------------------------------------------

root.mainloop()

