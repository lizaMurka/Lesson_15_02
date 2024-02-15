try:
    num_1 = float(input("Enter number:"))
    num_2 = float(input("Enter number:"))
    maths_action = (input("Enter a mathematical operation (+, -, *, /):"))

    match maths_action:
        case "+":
            print(num_1 + num_2)
        case "-":
            print(num_1 - num_2)
        case "*":
            print(num_1 * num_2)
        case "/":
            print(num_1 / num_2)

except ZeroDivisionError as error:
    print(f"ZeroDivesionError: {error}")
except ValueError as error:
    print(f"VelueError: {error}")
except Exception as error:
    print(f"Exception: {error}")


