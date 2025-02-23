import tkinter as tk


def click(value):
    add_input.set(add_input.get()+str(value))



def calculate():
    try:
        result = eval(add_input.get())
        add_input.set(result)
    except:
        add_input.set("Error")



def clear():
    add_input.set("")




