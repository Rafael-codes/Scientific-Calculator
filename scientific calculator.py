from tkinter import*
import math

#Creation of window
window = Tk()
window.title("Scientific Calculator")
window.geometry("400x560")
window.resizable(False, False)
display_text = StringVar()
display = Entry(window, textvariable=display_text,state="readonly", font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
display.grid(row=0, column=0, columnspan=5, ipadx=10, ipady=20, padx=10, pady=10, sticky="nsew")

#Creation of buttons
buttons = [
    ["Sin","Cos","Tan","Log","π"],
    ['(', ')', '^', '+', '√'],
    ['7', '8', '9', '/', 'e'],
    ['4', '5', '6', '*', 'C'],
    ['1', '2', '3', '-', '⌫'],
    ['.', '0', '00', '%','=']
]

#Function which evaluates math functions
def eval1(s):
    s = s.replace("Sin", "math.sin")
    s = s.replace("Cos", "math.cos")
    s = s.replace("Tan", "math.tan")
    s=s.replace("Log","math.log")
    s=s.replace("e","math.e")
    s=s.replace("^","**")
    s=s.replace("√","**0.5")
    s=s.replace("π","math.pi")
    try :
        return eval(s)
    except SyntaxError:
        return ""

#Display of entries
def on_button_click(char):
    if char=="=":
        current_text = display_text.get()
        display_text.set(eval1(current_text))
    elif char=="C":
        display_text.set("")
    elif char=="π":
        current_text = display_text.get()
        if current_text[-1]=="(":
            display_text.set(current_text+"π")
        elif current_text=="" or current_text[-1]=="/" or current_text[-1]=="*" or current_text[-1]=="%" or current_text[-1]=="+" or current_text[-1]=="-":
            display_text.set(current_text+"π")
        else:
            display_text.set(current_text + "*"+"π")
    elif char=="⌫":
        current_text=display_text.get()
        display_text.set(current_text[:len(current_text)-1])
    elif char=="^":
        current_text=display_text.get()
        display_text.set(current_text+"^")
    elif char=="√":
        current_text=display_text.get()
        display_text.set(current_text+"√")
    elif char=="e":
        current_text=display_text.get()
        display_text.set(current_text+"e^")
    elif char=="Sin" or char=="Cos" or char=="Tan" or char=="Log":
        current_text=display_text.get()
        display_text.set(current_text+char+"(")
    else:
        current_text = display_text.get()
        display_text.set(current_text + char)
    display.icursor(END)

#Aligning the buttons
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        btn = Button(window, text=char, font=("Arial", 16), width=6, height=2,
                        command=lambda ch=char: on_button_click(ch))
        btn.grid(row=r+1, column=c, padx=5, pady=5, sticky="nsew")
for i in range(5):
    window.grid_columnconfigure(i, weight=1)
for i in range(len(buttons)+1):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()

