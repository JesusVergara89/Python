from tkinter import *
from tkinter import filedialog

root=Tk()

fileRoute = ""
def abreFichero():
    global fileRoute
    fileRoute=filedialog.askopenfilenames(title="abrir")
    TextoFinal.config(text=fileRoute)

Button(root, text="abrir fichero", command=abreFichero).pack()

TextoFinal = Label(root)
TextoFinal.pack()

root.mainloop()