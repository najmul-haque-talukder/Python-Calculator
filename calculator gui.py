import tkinter as tk

# Function to update the input field
def button_click(value):
    entry_var.set(entry_var.get() + str(value))

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear the entry field
def clear():
    entry_var.set("")

# Main Tkinter window
root = tk.Tk()
root.title("Simple Calculator")

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Add buttons to the grid
for text, row, col in buttons:
    action = lambda x=text: button_click(x) if x != "=" else calculate()
    tk.Button(root, text=text, font=("Arial", 18), command=action, width=5, height=2).grid(row=row, column=col)

# Clear button
tk.Button(root, text="C", font=("Arial", 18), command=clear, width=5, height=2).grid(row=5, column=0, columnspan=4)

root.mainloop()