import ast

while True:
    try:
        value = input("Enter your calculation, (while you want to quite your calculation type 'exit') : ")
        if value.lower() == "exit":
            break
        result = eval(value)
        print("Result of", value, " is = ", result)

    except Exception as e:
        print("Error is : ", e)