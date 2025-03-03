import customtkinter as tk
import math



#-------------------------------------------------------------------------------------------------------------------------------------------------
def click(value):
    add.set(add.get() + str(value))


def factorial():
    try:
        num = int(add.get())
        add.set(math.factorial(num))
    except ValueError:
        add.set("Error")


def exit_program():
    root.quit()


def calculate():
    try:
        result = eval(add.get())
        add.set(result)
    except Exception as e:
        add.set("Error")


def toggle():
    value = add.get()
    if value.startswith("-"):
        add.set(value[1:])
    else:
        add.set("-" + value)


def clear():
    add.set("")


def backspace():
    add.set(add.get()[:-1])


def pi():
    add.set(add.get() + str(math.pi))


def square():
    num = float(add.get())
    add.set(num * num)


def power(value):
    add.set(add.get() + ("**" if value == "^" else str(value)))


def rootover():
    num = float(add.get())
    add.set(math.sqrt(num))


def sin_func():
    num = float(add.get())
    add.set("{:.2f}".format(math.sin(math.radians(num))))


def percent():
    num = float(add.get())
    add.set(num * 0.01)


def cos_func():
    num = float(add.get())
    add.set("{:.2f}".format(math.cos(math.radians(num))))


def log_function():
    try:
        num = float(add.get())
        if num <= 0:
            add.set("Error")
        else:
            add.set("{:.2f}".format(math.log(num)))  # Natural logarithm (base e)
    except ValueError:
        add.set("Error")


def ten():
    num = float(add.get())
    add.set("{:.2f}".format(math.sin(math.radians(num))))


# Conversion functions
def cm_to_m():
    try:
        num = float(entry2.get())
        result.set(f"{num / 100:.4f} meters")
    except ValueError:
        result.set("Error")


def m_to_cm():
    try:
        num = float(entry2.get())
        result.set(f"{num * 100:.4f} centimeters")
    except ValueError:
        result.set("Error")


def f_to_c():
    try:
        num = float(entry2.get())
        result.set(f"{(num - 32) * 5 / 9:.2f} °C")
    except ValueError:
        result.set("Error")


def c_to_f():
    try:
        num = float(entry2.get())
        result.set(f"{(num * 9 / 5) + 32:.2f} °F")
    except ValueError:
        result.set("Error")


def pixel_to_inch():
    try:
        num = float(entry2.get())
        result.set(f"{num / 96:.4f} inches")
    except ValueError:
        result.set("Error")


def inch_to_pixel():
    try:
        num = float(entry2.get())
        result.set(f"{num * 96:.0f} pixels")
    except ValueError:
        result.set("Error")


def min_to_hour():
    try:
        num = float(entry2.get())
        result.set(f"{num / 60:.2f} hours")
    except ValueError:
        result.set("Error")


def hour_to_min():
    try:
        num = float(entry2.get())
        result.set(f"{num * 60:.0f} minutes")
    except ValueError:
        result.set("Error")





# Functions to insert trigonometric/log expressions instead of calculating immediately
def insert_sin():
    try:
        num = float(add.get())
        add.set("{:.2f}".format(math.sin(math.radians(num))))
    except:
        add.set("Value Frist and type AC")

def insert_cos():
    try:
        num = float(add.get())
        add.set("{:.2f}".format(math.cos(math.radians(num))))
    except:
        add.set("Value Frist and type AC")

def insert_tan():
    try:
        num = float(add.get())
        add.set("{:.2f}".format(math.tan(math.radians(num))))
    except:
        add.set("Value Frist and type AC")

def insert_log():
    add.set(math.log)

# Function to calculate percentage
def percent(value):
    try:
        num = float(add.get())
        add.set(num * 0.01 * value )
    except ValueError:
        add.set("Error")
#-------------------------------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------------------------------------------
root = tk.CTk()
root.title("Najmul's Calculator")
root.geometry("500x600")
root.resizable(True, True)
#-------------------------------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------------------------------------------
add = tk.StringVar()
entry = tk.CTkEntry(root, textvariable=add, font=("Arial", 30), justify="right", corner_radius=10, width=450, height=50)
entry.grid(column=0, row=0, columnspan=5, ipady=30, padx=10, sticky="nsew")
#-------------------------------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------------------------------------------
buttons = (
    ("AC", 1, 0), ("Square", 1, 1), ("Root", 1, 2), ("^", 1, 3), ("Dlt", 1, 4),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3), ("%", 2, 4),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3), ("+/-", 3, 4),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3), (".", 4, 4),
    ("0", 5, 0), ("(", 5, 1), (")", 5, 2), ("+", 5, 3), ("=", 5, 4),
    ("log", 6, 0), ("!", 6, 1), ("sqrt", 6, 2), ("pi", 6, 3), ("log", 6, 4),
    ("sin", 7, 0), ("tan", 7, 1), ("cos", 7, 2), ("Adv", 7, 3)
)
#-------------------------------------------------------------------------------------------------------------------------------------------------

# Action mapping for buttons
for text, row, column in buttons:
    if text == "=":
        action = lambda x=text: calculate()
    elif text == "log":
        action = log_function
    elif text == "!":
        action = factorial
    elif text == "Square":
        action = square
    elif text == "AC":
        action = clear
    elif text == "+/-":
        action = toggle
    elif text == "^":
        action = lambda: power("^")
    elif text == "Dlt":
        action = backspace
    elif text == "sin":
        action = insert_sin
    elif text == "cos":
        action = insert_cos
    elif text == "tan":
        action = insert_tan
    elif text == "%":
        action = percent
    elif text =="Root":
        action= root
    elif text == "Adv":
        action = lambda: page2()
    else:
        action = lambda x=text: click(x)

    # Create buttons
    tk.CTkButton(root, text=text, font=("Arial", 18), command=action, height=70, width=100, corner_radius=10).grid(
        row=row, column=column, padx=10, pady=10)

#-------------------------------------------------------------------------------------------------------------------------------------------------





#-------------------------------------------------------------------------------------------------------------------------------------------------

# Advanced conversion window
def page2():
    page2 = tk.CTkToplevel(root)
    page2.title("Conversions")
    page2.geometry("400x600")
    page2.resizable(False, False)

    # Header label
    header_label = tk.CTkLabel(page2, text="Advanced Conversions", font=("Arial", 18), width=380, height=40, anchor="center")
    header_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

    # Input entry
    global entry2
    entry2 = tk.CTkEntry(page2, font=("Arial", 20), width=200, corner_radius=10)
    entry2.grid(row=1, column=0, columnspan=2, pady=10)

    # Output label
    global result
    result = tk.StringVar()
    output_label = tk.CTkLabel(page2, textvariable=result, font=("Arial", 16), width=250, height=40, anchor="center")
    output_label.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

    # Add conversion buttons in grid
    buttons = [
        ("Cm to M", cm_to_m),
        ("M to Cm", m_to_cm),
        ("F to C", f_to_c),
        ("C to F", c_to_f),
        ("Pixel to Inch", pixel_to_inch),
        ("Inch to Pixel", inch_to_pixel),
        ("Min to Hour", min_to_hour),
        ("Hour to Min", hour_to_min),
    ]

    row = 3
    for text, command in buttons:
        tk.CTkButton(page2, text=text, font=("Arial", 14), command=command, height=30, width=180, corner_radius=10).grid(row=row, column=0, columnspan=2, padx=10, pady=10)
        row += 1

#-------------------------------------------------------------------------------------------------------------------------------------------------








# Responsive layout configuration
for i in range(5):
    root.grid_columnconfigure(i, weight=1, uniform="col")
for i in range(8):
    root.grid_rowconfigure(i, weight=1, uniform="row")

root.mainloop()
