from tkinter import *

root = Tk()

my_frame = Frame(root)

root.title("Calculator")

my_frame.pack()

my_frame.config(background="#9EE2CE", padx=30, pady=30)

#--------------Screen-------------------------------------------
screen = Entry(my_frame) 
screen.grid(row=1,column=1,padx=10,pady=10, columnspan=4)
screen.config(background="black", fg="#03f943", justify="right")
#---------------------------------------------------------------

#--------------Line1-------------------------------------------
button7 = Button(my_frame, text="7", width=3, bd=5, relief="solid")
button7.grid(row=2,column=1)
button8 = Button(my_frame, text="8", width=3, bd=5, relief="solid")
button8.grid(row=2,column=2)
button9 = Button(my_frame, text="9", width=3, bd=5, relief="solid")
button9.grid(row=2,column=3)
buttonDiv = Button(my_frame, text="/", width=3, bd=5, relief="solid")
buttonDiv.grid(row=2,column=4)
#---------------------------------------------------------------

#--------------Line2-------------------------------------------
button4 = Button(my_frame, text="4", width=3, bd=5, relief="solid")
button4.grid(row=3,column=1)
button5 = Button(my_frame, text="5", width=3, bd=5, relief="solid")
button5.grid(row=3,column=2)
button6 = Button(my_frame, text="6", width=3, bd=5, relief="solid")
button6.grid(row=3,column=3)
buttonMulti = Button(my_frame, text="x", width=3, bd=5, relief="solid")
buttonMulti.grid(row=3,column=4)
#---------------------------------------------------------------

#--------------Line3-------------------------------------------
button1 = Button(my_frame, text="1", width=3, bd=5, relief="solid")
button1.grid(row=4,column=1)
button2 = Button(my_frame, text="2", width=3, bd=5, relief="solid")
button2.grid(row=4,column=2)
button3 = Button(my_frame, text="3", width=3, bd=5, relief="solid")
button3.grid(row=4,column=3)
buttonSum = Button(my_frame, text="+", width=3, bd=5, relief="solid")
buttonSum.grid(row=4,column=4)
#---------------------------------------------------------------

#--------------Line3-------------------------------------------
buttonDel = Button(my_frame, text="Del", width=3, bd=5, relief="solid")
buttonDel.grid(row=5,column=1)
buttonDot = Button(my_frame, text=".", width=3, bd=5, relief="solid")
buttonDot.grid(row=5,column=2)
buttonSubs = Button(my_frame, text="-", width=3, bd=5, relief="solid")
buttonSubs.grid(row=5,column=3)
buttonEqual = Button(my_frame, text="=", width=3, bd=5, relief="solid")
buttonEqual.grid(row=5,column=4)
#---------------------------------------------------------------


root.mainloop()