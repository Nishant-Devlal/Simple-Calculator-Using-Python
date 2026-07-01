from tkinter import*
from ctypes import windll
import os

root=Tk()
root.title("Calculator")
root.geometry("430x620")
root.resizable(False,False)
root.configure(bg="Black")
windll.shcore.SetProcessDpiAwareness(1)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
        
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)

equation=" "

def show(value):
    global equation
    equation+=value
    a.config(text=equation)

def plusminus():
    global equation
    equation=f"-{equation}"
    a.config(text=equation)

def remove():
    global equation
    equation=equation[:-1]
    a.config(text=equation)
    
def clear():
    global equation
    equation=" "
    a.config(text=equation)

def calculate():
    global equation
    result=" "
    if equation!=" ":
        try:
            equation=equation.replace('÷','/')
            equation=equation.replace("√","**0.5")
            equation=equation.replace("×","*")
            equation=equation.replace("²","**2")
            result=eval(equation)
        except:
            result="error"
            equation=" "
    a.config(text=result)


########### Icon #############
icon=PhotoImage(file=resource_path("Calcicon.png"))
root.iconphoto(False,icon)

########### Label ############
f1=Frame(root, bg="White", width=420, height=110)
f1.place(x=3, y=50)
a=Label(f1, border=0, width=23, height=3, text=" ", font=("Arial 23"), bg="Black", fg="White")
a.place(x=2,y=1)
Label(root, border=0, width=8, height=1, text="Standard", font=("Arial 18 bold"),
        bg="Black", fg="White").place(x=0,y=15)

########### Buttons ###########
Button(root, pady=14, border=0, text="%", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("%")).place(x=5,y=170)

Button(root, pady=14, border=0, text="CE", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=remove).place(x=110,y=170)

Button(root, pady=14, border=0, text="C", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=clear).place(x=215,y=170)

Button(root, pady=14, border=0, text="❎", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=remove).place(x=320,y=170)

Button(root, pady=14, border=0, text="1/x", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("1/")).place(x=5,y=245)

Button(root, pady=14, border=0, text="x²", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("²")).place(x=110,y=245)

Button(root, pady=14, border=0, text="²√x", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("√")).place(x=215,y=245)

Button(root, pady=14, border=0, text="÷", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White",command=lambda:show("÷")).place(x=320,y=245)

Button(root, pady=14, border=0, text="7", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("7")).place(x=5,y=320)

Button(root, pady=14, border=0, text="8", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("8")).place(x=110,y=320)

Button(root, pady=14, border=0, text="9", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("9")).place(x=215,y=320)

Button(root, pady=14, border=0, text="×", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("×")).place(x=320,y=320)

Button(root, pady=14, border=0, text="4", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("4")).place(x=5,y=395)

Button(root, pady=14, border=0, text="5", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("5")).place(x=110,y=395)

Button(root, pady=14, border=0, text="6", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("6")).place(x=215,y=395)

Button(root, pady=14, border=0, text="-", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("-")).place(x=320,y=395)

Button(root, pady=14, border=0, text="1", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("1")).place(x=5,y=470)

Button(root, pady=14, border=0, text="2", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("2")).place(x=110,y=470)

Button(root, pady=14, border=0, text="3", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717",fg="White", command=lambda:show("3")).place(x=215,y=470)

Button(root, pady=14, border=0, text="+", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("+")).place(x=320,y=470)

Button(root, pady=14, border=0, text="+/-", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=plusminus).place(x=5,y=545)

Button(root, pady=14, border=0, text="0", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show("0")).place(x=110,y=545)

Button(root, pady=14, border=0, text=".", width=7, height=1, anchor='center', font="Arial 18",
       bg="#171717", fg="White", command=lambda:show(".")).place(x=215,y=545)

Button(root, pady=14, border=0, text="=", width=7, height=1, anchor='center', font="Arial 18",
       bg="#9FD5E8", fg="Black", command=calculate).place(x=320,y=545)

root.mainloop()
