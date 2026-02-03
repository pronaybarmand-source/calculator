from tkinter import *

# main window
a=Tk()
a.geometry("500x500")
a.title("GUI Calculator ")
equation=StringVar()
b=""

def calculator(event):
    global b
    char=event.widget.cget("text")
    if char=="CLEAR":
        b=""
        equation.set("")
    elif char =="=":
        answer=eval(equation.get())
        equation.set(answer)
        b=str(answer)

    else:

        b=b+char
        equation.set(b)

    
def backspace():
    entry.delete((len(entry.get()))-1,END)    


#entry process
entry=Entry(a,
            font=("Arial",30),
            relief=SUNKEN,
            borderwidth=10,
            textvariable=equation)#relief is used for giving border
entry.grid(row=0,column=0,columnspan=4)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


button=Button(a,
              text="9",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=1,column=0)
button.bind("<Button-1>",calculator)

button=Button(a,
              text="8",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=1,column=1)
button.bind("<Button-1>",calculator)

button=Button(a,
              text="7",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=1,column=2)
button.bind("<Button-1>",calculator)

button=Button(a,
              text="+",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=1,column=3)
button.bind("<Button-1>",calculator)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
button=Button(a,
              text="6",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=6)
button.grid(row=2,column=0)
button.bind("<Button-1>",calculator)

button=Button(a,
              text="5",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=2,column=1)
button.bind("<Button-1>",calculator)

button=Button(a,
              text="4",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=2,column=2)
button.bind("<Button-1>",calculator)

button=Button(a,
              text="-",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=2,column=3)
button.bind("<Button-1>",calculator)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
button=Button(a,
              text="3",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=3,column=0)
button.bind("<Button-1>",calculator)

button=Button(a,
              text="2",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=3,column=1)
button.bind("<Button-1>",calculator)

button=Button(a,
              text="1",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=3,column=2)
button.bind("<Button-1>",calculator)

button=Button(a,
              text="*",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=3,column=3)
button.bind("<Button-1>",calculator)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
button=Button(a,
              text=".",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=6)
button.grid(row=4,column=0)
button.bind("<Button-1>",calculator)

button=Button(a,
              text="0",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=4,column=1)
button.bind("<Button-1>",calculator)

button=Button(a,
              text="/",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=4,column=2)
button.bind("<Button-1>",calculator)

button=Button(a,
              text="=",
              font=("Arial",30),
              height=1,
              width=4,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=4,column=3)
button.bind("<Button-1>",calculator)
#...........................................clearbutton
button=Button(a,
              text="CLEAR",
              font=("Arial",30),
              width=9,
              relief=GROOVE,borderwidth=4)
button.grid(row=5,column=0,columnspan=2)
button.bind("<Button-1>",calculator) 
button=Button(a,
              text="BACKSPACE",
              command=backspace,
              font=("Arial",30),
              width=9,
              relief=GROOVE,
              borderwidth=4)
button.grid(row=5,column=2,columnspan=2)
# button.bind("<Button-1>",calculator) 

a.mainloop()