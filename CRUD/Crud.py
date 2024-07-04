from tkinter import *
from tkinter import messagebox
import sqlite3
from conectionBBDD import *
from Salir import *
from Create import *
from Delete import *
from Leer import *
from Limpiar import *
from Actualizar import *
from Acercade import *

root = Tk()

#----------Variables------------------------------------
screenID = StringVar()
screenName=StringVar()
screenPassword=StringVar()
screenApellido=StringVar()
screenDireccion=StringVar()
#-------------------------------------------------------

root.title("CRUD with python")
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300, background="#2F4F4F")

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBD)
bbddMenu.add_command(label="Salir", command=lambda:salirAplicación(root))

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=lambda:cleanData(screenID,screenName, screenPassword, screenApellido,screenDireccion, cuadroTexto))

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=lambda:createUser(screenName.get(),screenPassword.get(),screenApellido.get(),screenDireccion.get(),cuadroTexto.get("1.0", END)))
crudMenu.add_command(label="Leer", command=lambda:readUser(screenID.get(),screenID,screenName, screenPassword, screenApellido,screenDireccion, cuadroTexto))
crudMenu.add_command(label="Actualizar", command=lambda:updateUser(screenID.get(),screenName.get(),screenPassword.get(),screenApellido.get(),screenDireccion.get(),cuadroTexto.get("1.0", END)))
crudMenu.add_command(label="Borrar", command=lambda:deleteUser(screenID.get()))

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de", command=About)

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#----------frames----------------------------------------

input_frame=Frame(root)
input_frame.pack()
input_frame.config(background="#2F4F4F")

btn_frame=Frame(root)
btn_frame.pack()
btn_frame.config(background="#2F4F4F")

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

cuadroID = Entry(input_frame, textvariable=screenID)
cuadroID.grid(row=0, column=1, padx=10,pady=10)

cuadroNombre = Entry(input_frame, textvariable=screenName)
cuadroNombre.grid(row=1, column=1, padx=10,pady=10)

cuadroContrasena = Entry(input_frame, textvariable=screenPassword)
cuadroContrasena.grid(row=2, column=1, padx=10,pady=10)
cuadroContrasena.config(show="*")

cuadroApellido = Entry(input_frame, textvariable=screenApellido)
cuadroApellido.grid(row=3, column=1, padx=10,pady=10)

cuadroDireccion = Entry(input_frame, textvariable=screenDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10,pady=10)

cuadroTexto = Text(input_frame, width=27, height=5)
cuadroTexto.grid(row=5, column=1, padx=10,pady=10)
scrollvert=Scrollbar(input_frame, command=cuadroTexto.yview)
scrollvert.grid(row=5,column=2, sticky="nsew")

cuadroTexto.config(yscrollcommand=scrollvert.set)

#---------------------------------------------------------

#----------Btns----------------------------------------
btnCrear = Button(btn_frame, text="Create", command=lambda:createUser(screenName.get(),screenPassword.get(),screenApellido.get(),screenDireccion.get(),cuadroTexto.get("1.0", END)))
btnCrear.grid(row=1, column=0, sticky="e", padx=10,pady=10)

btnLeer = Button(btn_frame, text="Read", command=lambda:readUser(screenID.get(),screenID,screenName, screenPassword, screenApellido,screenDireccion, cuadroTexto))
btnLeer.grid(row=1, column=1, sticky="e", padx=10,pady=10)

btnActualizar = Button(btn_frame, text="Update",command=lambda:updateUser(screenID.get(),screenName.get(),screenPassword.get(),screenApellido.get(),screenDireccion.get(),cuadroTexto.get("1.0", END)))
btnActualizar.grid(row=1, column=2, sticky="e", padx=10,pady=10)

btnEliminar = Button(btn_frame, text="Delete", command=lambda:deleteUser(screenID.get()))
btnEliminar.grid(row=1, column=3, sticky="e", padx=10,pady=10)
#---------------------------------------------------------

root.mainloop()

