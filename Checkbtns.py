from tkinter import *

root=Tk()
root.title("Check btns")

playa = IntVar()
Bosque = IntVar()
Desierto = IntVar()

def travelOptions():
    optionChoose=""
    if playa.get()==1:
        optionChoose+=" playa"
    if Bosque.get()==1:
        optionChoose+=" Bosque"
    if Desierto.get()==1:
        optionChoose+=" Desierto"
    TextoFinal.config(text=optionChoose)

image=PhotoImage(file="/Volumes/harkdisk/Projects/python/cars.png")
Label(root, image=image).pack()

my_frame=Frame(root)
my_frame.pack()

Label(my_frame, text="Elige destinos", width=50).pack()

Checkbutton(my_frame, text="playa", variable=playa, onvalue=1, offvalue=0, command=travelOptions).pack()
Checkbutton(my_frame, text="Bosque", variable=Bosque, onvalue=1, offvalue=0, command=travelOptions).pack()
Checkbutton(my_frame, text="Desierto", variable=Desierto, onvalue=1, offvalue=0, command=travelOptions).pack()

TextoFinal = Label(my_frame)
TextoFinal.pack()

root.mainloop()
