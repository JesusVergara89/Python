from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miImagen = PhotoImage(file="/Volumes/harkdisk/Projects/python/PrimeraInterface/cars.png")
milabel1= Label(miFrame, image=miImagen).place(x=0, y=0)
miLabel=Label(miFrame, text="Hola soy Jesus", fg="yellow", font=("Comic Sans MS",12))
miLabel.place(x=100, y=100)
#Si no se van a usar mas las variables miFrame, podemos poner asi: 
#Label(miFrame, text="Hola soy Jesus", fg="yellow", font=("Comic Sans MS",12)).place(x=100, y=100)

root.mainloop()