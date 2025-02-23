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
root.title("Najmuls Calculator")


add = tk.StringVar()
entry = tk.Entry(root, textvariable=add, bd=10, font=("Arial", 20), justify="right", relief="ridge")
entry.grid(column=0, row=0, columnspan=4)



buttons = [
    ("7", 0, 1), ("8", 1, 1), ("9", 2, 1), ("/", 3, 1),
    ("4", 0, 2), ("5", 1, 2), ("6", 2, 2), ("*", 3, 2),
    ("1", 0, 3), ("2", 1, 3), ("3", 2, 3), ("-", 3, 3),
    ("0", 0, 4), (".", 1, 4), ("=", 2, 4), ("+", 3, 4)
]


for text, column, row in buttons:
    action = lambda x=text: click(x)  if x != "=" else calculate()
    tk.Button(root, text=text, font=("Arial", 18), command=action, height=2, width=5).grid(row=row, column=column)


tk.Button(root, text="AC", font=("Arial", 18), command=clear, height=2, width=22).grid(row=5, column=0, columnspan=4)

root.mainloop()