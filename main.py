import tkinter
from tkinter import *
from tkinter import messagebox

var = ""
A = 0
operator = ""
memory = ""
a = 0
history = []


def button_pm():
    global var
    if var > '0':
        var = '-' + var
    else:
        str = var[1:]
        str = '+' + str
        var = str
    the_data.set(var)


def button_1():
    global var
    var = var + "1"
    the_data.set(var)


def button_2():
    global var
    var = var + "2"
    the_data.set(var)


def button_3():
    global var
    var = var + "3"
    the_data.set(var)


def button_4():
    global var
    var = var + "4"
    the_data.set(var)


def button_5():
    global var
    var = var + "5"
    the_data.set(var)


def button_6():
    global var
    var = var + "6"
    the_data.set(var)


def button_7():
    global var
    var = var + "7"
    the_data.set(var)


def button_8():
    global var
    var = var + "8"
    the_data.set(var)


def button_9():
    global var
    var = var + "9"
    the_data.set(var)


def button_0():
    global var
    var = var + "0"
    the_data.set(var)


def button_ms():
    global var
    global memory
    memory = var


def button_mr():
    global var
    global memory
    var = memory
    the_data.set(var)


def button_mc():
    global var
    global memory
    memory = ""


def button_mp():
    global var
    global memory
    memory = float(memory)
    var = float(var)
    memory += var


def button_mm():
    global var
    global memory
    memory = float(memory)
    var = float(var)
    memory -= var


def button_point():
    global var
    global operator
    q = var.count(".")
    if var[-1] != ".":
        var = var + "."
    if q > 0 and operator == "":
        messagebox.showerror('Too many points')
        var = ""
    the_data.set(var)


def button_Add():
    global A
    global var
    global operator
    A = float(var)
    operator = "+"
    var = var + "+"
    the_data.set(var)


def button_Sub():
    global A
    global var
    global operator
    A = float(var)
    operator = "-"
    var = var + "-"
    the_data.set(var)


def button_Mul():
    global A
    global var
    global operator
    A = float(var)
    operator = "*"
    var = var + "*"
    the_data.set(var)


def button_Div():
    global A
    global var
    global operator
    A = float(var)
    operator = "/"
    var = var + "/"
    the_data.set(var)


def button_Equal():
    global A
    global var
    global operator
    global history
    A = float(var)
    history = A
    operator = "="
    var = var + "="
    the_data.set(var)
    the_history.set(history)


def button_C():
    global A
    global var
    global operator
    var = ""
    A = 0
    operator = ""
    the_data.set(var)


def res():
    global A
    global operator
    global var
    global a
    var2 = var
    if operator == "+":
        a = float((var2.split("+")[1]))
        x = A + a
        the_data.set(x)
        var = str(x)
    elif operator == "-":
        a = float((var2.split("-")[1]))
        x = A - a
        the_data.set(x)
        var = str(x)
    elif operator == "*":
        a = float((var2.split("*")[1]))
        x = A * a
        the_data.set(x)
        var = str(x)
    elif operator == "/":
        a = float((var2.split("/")[1]))
        if a == 0:
            messagebox.showerror("Division by 0 Not Allowed.")
            A == ""
            var = ""
            the_data.set(var)
        else:
            x = float(A / a)
            the_data.set(x)
            var = str(x)


guiWindow = tkinter.Tk()
guiWindow.geometry("500x500+400+400")
guiWindow.resizable(False, False)
guiWindow.title("Calculator")

the_data = StringVar()
guiLabel = Label(
    guiWindow,
    text="Label",
    anchor=SE,
    font=("Cambria Math", 20),
    textvariable=the_data,
    background="#ffffff",
    fg="#000000"
)
guiLabel.pack(expand=True, fill="both")

frameOne = Frame(guiWindow, bg="#000000")
frameOne.pack(expand=True, fill="both")

frameTwo = Frame(guiWindow, bg="#000000")
frameTwo.pack(expand=True, fill="both")

frameThree = Frame(guiWindow, bg="#000000")
frameThree.pack(expand=True, fill="both")

frameFour = Frame(guiWindow, bg="#000000")
frameFour.pack(expand=True, fill="both")

frameFive = Frame(guiWindow, bg="#000000")
frameFive.pack(expand=True, fill="both")

the_history = DoubleVar()
historyLabel = Label(
    guiWindow,
    text="History",
    anchor=SW,
    font=("Cambria Math", 20),
    textvariable=the_history,
    background="#ffffff",
    fg="#ff0000"
)
historyLabel.pack(expand=True, fill="both")

buttonPOINT = Button(
    frameOne,
    text=".",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_point
)
buttonPOINT.pack(side=LEFT, expand=True, fill="both")

buttonONE = Button(
    frameOne,
    text="1",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_1
)
buttonONE.pack(side=LEFT, expand=True, fill="both")

buttonTWO = Button(
    frameOne,
    text="2",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_2
)
buttonTWO.pack(side=LEFT, expand=True, fill="both")

buttonTHREE = Button(
    frameOne,
    text="3",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_3
)
buttonTHREE.pack(side=LEFT, expand=True, fill="both")

buttonC = Button(
    frameOne,
    text="C",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_C
)
buttonC.pack(side=LEFT, expand=True, fill="both")

buttonFOUR = Button(
    frameTwo,
    text="4",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_4
)
buttonFOUR.pack(side=LEFT, expand=True, fill="both")

buttonFIVE = Button(
    frameTwo,
    text="5",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_5
)
buttonFIVE.pack(side=LEFT, expand=True, fill="both")

buttonSIX = Button(
    frameTwo,
    text="6",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_6
)
buttonSIX.pack(side=LEFT, expand=True, fill="both")

buttonADD = Button(
    frameTwo,
    text="+",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_Add
)
buttonADD.pack(side=LEFT, expand=True, fill="both")

buttonSEVEN = Button(
    frameThree,
    text="7",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_7
)
buttonSEVEN.pack(side=LEFT, expand=True, fill="both")

buttonEIGHT = Button(
    frameThree,
    text="8",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_8
)
buttonEIGHT.pack(side=LEFT, expand=True, fill="both")

buttonNINE = Button(
    frameThree,
    text="9",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_9
)
buttonNINE.pack(side=LEFT, expand=True, fill="both")

buttonSUB = Button(
    frameThree,
    text="-",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_Sub
)
buttonSUB.pack(side=LEFT, expand=True, fill="both")

buttonZERO = Button(
    frameFour,
    text="0",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_0
)
buttonZERO.pack(side=LEFT, expand=True, fill="both")

buttonMUL = Button(
    frameFour,
    text="*",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_Mul
)
buttonMUL.pack(side=LEFT, expand=True, fill="both")

buttonDIV = Button(
    frameFour,
    text="/",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button_Div
)
buttonDIV.pack(side=LEFT, expand=True, fill="both")

buttonEQUAL = Button(
    frameFour,
    text="=",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=res
)
buttonEQUAL.pack(side=LEFT, expand=True, fill="both")

buttonMS = Button(
    frameFive,
    text="MS",
    font=("Cambria", 22),
    relief=GROOVE,
    bg="black",
    fg="white",
    border=0,
    command=button_ms
)
buttonMS.pack(side=LEFT, expand=True, fill="both")

buttonMR = Button(
    frameFive,
    text="MR",
    font=("Cambria", 22),
    relief=GROOVE,
    bg="black",
    fg="white",
    border=0,
    command=button_mr
)
buttonMR.pack(side=LEFT, expand=True, fill="both")

buttonMC = Button(
    frameFive,
    text="MC",
    font=("Cambria", 22),
    relief=GROOVE,
    bg="black",
    fg="white",
    border=0,
    command=button_mc
)
buttonMC.pack(side=LEFT, expand=True, fill="both")

buttonMP = Button(
    frameFive,
    text="M+",
    font=("Cambria", 22),
    relief=GROOVE,
    bg="black",
    fg="white",
    border=0,
    command=button_mp
)
buttonMP.pack(side=LEFT, expand=True, fill="both")

buttonMM = Button(
    frameFive,
    text="M-",
    font=("Cambria", 22),
    relief=GROOVE,
    bg="black",
    fg="white",
    border=0,
    command=button_mm
)
buttonMM.pack(side=LEFT, expand=True, fill="both")

buttonPM = Button(
    frameFive,
    text="+-",
    font=("Cambria", 22),
    relief=GROOVE,
    bg="black",
    fg="white",
    border=0,
    command=button_pm
)
buttonPM.pack(side=LEFT, expand=True, fill="both")

guiWindow.mainloop()
