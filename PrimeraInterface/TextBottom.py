from tkinter import *

root = Tk()

miFrame=Frame(root, width=250, height=250)
miFrame.pack()

miNombre=StringVar()

## - Label's - ###########################
nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0,column=0, sticky="e", padx=5,pady=5)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1,column=0, sticky="e", padx=5,pady=5)

apellidoLabel=Label(miFrame, text="Password: ")
apellidoLabel.grid(row=2,column=0, sticky="e", padx=5,pady=5)

direccionLabel=Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=3,column=0, sticky="e", padx=5,pady=5)

comentariosLabel=Label(miFrame, text="Escribe un comentario: ")
comentariosLabel.grid(row=4,column=0, sticky="e", padx=5,pady=5)
#############################################


## - Text's - ###########################
textoComentarios = Text(miFrame, width=25, height=9)
textoComentarios.grid(row=4, column=1)

scrollvertical= Scrollbar(miFrame, command=textoComentarios.yview)
scrollvertical.grid(row=4,column=2, sticky="nsew")
textoComentarios.config(yscrollcommand=scrollvertical.set)
#############################################


## - Entry's - ###########################
cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0,column=1)
cuadroNombre.config(fg="red", justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1)

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=2,column=1)
cuadroPassword.config(show="*")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1)
#############################################


## - Bottom's - ###########################
def codigoBtn():
    miNombre.set("Juan")

botonEnvio = Button(root, text="Enviar", command=codigoBtn)
botonEnvio.pack()
#############################################

root.mainloop()
