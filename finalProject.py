import tkinter as tk


def click(value):
    add.set(add.get()+str(value))


def calculate():
    result = eval(add.get())
    add.set(result)


def clear():
    add.set("")



root = tk.Tk()
root.title("Najmuls Calculator : by Python")


add = tk.StringVar()
entry = tk.Entry(root, textvariable=add, font=("Arial", 20), bd=10, justify="right", relief="ridge")
entry.grid(row=0, column=0, columnspan=4 )



buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for text, row, column in buttons:
    action = lambda x=text: click(x) if x!= "=" else calculate()
    tk.Button(root, text=text, command=action, font=("Arial", 18), height=2, width=5).grid(row=row, column=column)


tk.Button(root, text = "AC", command=clear, font=("Arial", 18),  height=2, width=22).grid( row = 5, column=0, columnspan=4)


root.mainloop()