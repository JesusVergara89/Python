from tkinter import *

root = Tk()

miFrame=Frame(root, width=250, height=250)
miFrame.pack()

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0,column=0, sticky="e", padx=5,pady=5)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1,column=0, sticky="e", padx=5,pady=5)

apellidoLabel=Label(miFrame, text="Password: ")
apellidoLabel.grid(row=2,column=0, sticky="e", padx=5,pady=5)

direccionLabel=Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=3,column=0, sticky="e", padx=5,pady=5)

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1)
cuadroNombre.config(fg="red", justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1)

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=2,column=1)
cuadroPassword.config(show="*")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1)

root.mainloop()
