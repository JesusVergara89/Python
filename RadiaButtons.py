from tkinter import *

root = Tk()

my_frame = Frame(root)

my_frame.pack()

varOption = IntVar()

def printValues():
    if varOption.get()==1:
        etiqueta.config(text="Masculino")
    else:
        etiqueta.config(text="Femenino")

Radiobutton(my_frame, text="Masculino", variable=varOption, value=1, command=printValues).pack()
Radiobutton(my_frame, text="Femenino", variable=varOption, value=2, command=printValues).pack()

etiqueta=Label(my_frame)
etiqueta.pack()


root.mainloop()

