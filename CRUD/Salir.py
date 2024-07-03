from tkinter import messagebox

def salirAplicación(data):
    value=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

    if value == "yes":
        data.destroy()

        