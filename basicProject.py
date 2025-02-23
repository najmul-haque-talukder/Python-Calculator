while True:
    try:
        value = input("Enter the Calculation(if you want to quite - type 'exit') : ")
        if value.lower()== "exit":
            break

        result = eval(value)
        print("Result of '",value, "' is : ", result )
        print("")

    except Exception as e:
        print("Error is : ", e)
