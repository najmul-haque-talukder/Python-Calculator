import tkinter as tk



# input from click
def click(value):
    add.set(entry.get()+str(value))
    


# calculation
def calculate():
    try:
        result = eval(add.get())
        add.set(result)
    except:
        add.set("Error")



# clear
def clear():
    add.set("")


def backspace():
    currentText = add.get()
    add.set(currentText[:-1])


 #tkinter window
root = tk.Tk()
root.title("Najmuls Calculator")



#entry field
add = tk.StringVar()
entry = tk.Entry(root, textvariable=add, font=("Arial", 20), bd=10, relief="ridge", justify="right")
entry.grid(column=0, row=0, columnspan=4)


#---------------------------------------------------------------------
buttons = [
    ("7", 0, 1), ("8", 1, 1), ("9", 2, 1), ("/", 3, 1),
    ("4", 0, 2), ("5", 1, 2), ("6", 2, 2), ("*", 3, 2),
    ("1", 0, 3), ("2", 1, 3), ("3", 2, 3), ("-", 3, 3),
    ("0", 0, 4), (".", 1, 4), ("=", 2, 4), ("+", 3, 4)
]



for text, column, row in buttons:
    action = lambda x=text : click(x) if x != "=" else calculate()
    tk.Button(root, text=text, font=("arial", 18), command=action, width=5, height=2).grid(row=row, column=column)


tk.Button(root, text="AC", font=("Arial", 18), command=clear, width=25, height=2).grid(row=5, column=0, columnspan=4)  # Fully fills last row


root.mainloop()



