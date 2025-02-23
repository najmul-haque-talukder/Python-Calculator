import tkinter as tk

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Arial", 20))
entry.pack()

def calculate():
    try:
        entry.insert(tk.END, " = " + str(eval(entry.get())))
    except:
        entry.insert(tk.END, " Error")

tk.Button(root, text="Calculate", command=calculate).pack()

root.mainloop()