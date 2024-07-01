from tkinter import *

root = Tk()

my_frame = Frame(root)

root.title("Calculator")

my_frame.pack()

my_frame.config(background="#9EE2CE", padx=30, pady=30)

#-----global variables----------------
result=""
total = 0
sign = ""

#--------------Screen-------------------------------------------
screenNumber=StringVar()
screen = Entry(my_frame, textvariable=screenNumber) 
screen.grid(row=1,column=1,padx=10,pady=10, columnspan=4)
screen.config(background="black", fg="#03f943", justify="right")
#---------------------------------------------------------------

#--------------Line1-------------------------------------------
button7 = Button(my_frame, text="7", width=3, bd=5, relief="solid", command=lambda:numberPressed('7'))
button7.grid(row=2,column=1)
button8 = Button(my_frame, text="8", width=3, bd=5, relief="solid", command=lambda:numberPressed('8'))
button8.grid(row=2,column=2)
button9 = Button(my_frame, text="9", width=3, bd=5, relief="solid", command=lambda:numberPressed('9'))
button9.grid(row=2,column=3)
buttonDiv = Button(my_frame, text="/", width=3, bd=5, relief="solid")
buttonDiv.grid(row=2,column=4)
#---------------------------------------------------------------

#--------------Line2-------------------------------------------
button4 = Button(my_frame, text="4", width=3, bd=5, relief="solid", command=lambda:numberPressed('4'))
button4.grid(row=3,column=1)
button5 = Button(my_frame, text="5", width=3, bd=5, relief="solid", command=lambda:numberPressed('5'))
button5.grid(row=3,column=2)
button6 = Button(my_frame, text="6", width=3, bd=5, relief="solid", command=lambda:numberPressed('6'))
button6.grid(row=3,column=3)
buttonMulti = Button(my_frame, text="x", width=3, bd=5, relief="solid")
buttonMulti.grid(row=3,column=4)
#---------------------------------------------------------------

#--------------Line3-------------------------------------------
button1 = Button(my_frame, text="1", width=3, bd=5, relief="solid", command=lambda:numberPressed('1'))
button1.grid(row=4,column=1)
button2 = Button(my_frame, text="2", width=3, bd=5, relief="solid", command=lambda:numberPressed('2'))
button2.grid(row=4,column=2)
button3 = Button(my_frame, text="3", width=3, bd=5, relief="solid", command=lambda:numberPressed('3'))
button3.grid(row=4,column=3)
buttonSum = Button(my_frame, text="+", width=3, bd=5, relief="solid", command=lambda:suma(screenNumber.get()))
buttonSum.grid(row=4,column=4)
#---------------------------------------------------------------

#--------------Line3-------------------------------------------
buttonZero = Button(my_frame, text="0", width=3, bd=5, relief="solid", command=lambda:numberPressed('0'))
buttonZero.grid(row=5,column=1)
buttonDot = Button(my_frame, text=".", width=3, bd=5, relief="solid")
buttonDot.grid(row=5,column=2)
buttonSubs = Button(my_frame, text="-", width=3, bd=5, relief="solid", command=lambda:resta(screenNumber.get()))
buttonSubs.grid(row=5,column=3)
buttonEqual = Button(my_frame, text="=", width=3, bd=5, relief="solid", command=lambda:theResult())
buttonEqual.grid(row=5,column=4)
#---------------------------------------------------------------

#--------------Line4-------------------------------------------
buttonDel = Button(my_frame, text="Del", width=3, bd=5, relief="solid", command=lambda:delScreen())
buttonDel.grid(row=6,column=4)
#---------------------------------------------------------------

#--------------Functions----------------------------------------
def numberPressed(num):
    global result
    if result != "":
        screenNumber.set(num)
        result = ""
    else:
        screenNumber.set(screenNumber.get() + num)
 
def delScreen():
    global result
    global total
    screenNumber.set('')
    result = ""
    total = 0

def suma(num):
    global result
    global total
    global sign
    total += float(num)
    result = "addition"
    sign = "+"
    screenNumber.set(total)

def resta(num):
    global result
    global total
    global sign
    if total == 0:
        total = float(num)
    else:
        total = total - float(num)
    result = "resta"
    sign = "-"
    screenNumber.set(total)

def theResult():
    global total
    if sign == "+":
        screenNumber.set(total + float(screenNumber.get()))
    elif sign == "-":
        screenNumber.set(total - float(screenNumber.get()))
    total = 0




root.mainloop()