from tkinter import *

raiz=Tk()

raiz.title("Ventana de prueba")

raiz.config(bg="yellow")

raiz.config(bd=10)

raiz.config(relief="sunken")

raiz.config(cursor="pirate")

miFrame=Frame()

miFrame.pack()

miFrame.config(bg="red")

miFrame.config(width="200", height="100")

raiz.mainloop()