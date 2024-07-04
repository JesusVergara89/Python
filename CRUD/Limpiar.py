from tkinter import *
from tkinter import messagebox

def cleanData(screenID,screenName, screenPassword, screenApellido,screenDireccion, cuadroTexto):
    screenID.set("")
    screenName.set("")
    screenPassword.set("")
    screenApellido.set("")
    screenDireccion.set("")
    cuadroTexto.delete('0.0', END)
    messagebox.showinfo("CRUD", "Campos limpiados éxito")
  