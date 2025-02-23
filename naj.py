import tkinter as tk


def click(value):
    add.set(add.get()+str(value))


def calculate():
    try:
        result = eval(add.get())
        add.set(result)
    except:
        add.set("Error")


def clear():
    add.set("")



root = tk.Tk()
root.title("Najmuls Developer")



add = tk.StringVar()
entry = tk.Entry(
    root,
    textvariable= add,
    bd=10,
    font= ("Arial", 20),
    justify="right",
    relief="ridge"
)
entry.grid(column=0, row=0, columnspan=4)




