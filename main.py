try:

    day =int(input("Keep the day of the week number (1-7):"))

    if day > 7:
        raise ValueError("Введіть число від 1 до 7.")

    match day:
        case 1:
         print("Monday")
        case 2:
         print("Tuesday")
        case 3:
         print("Wednesday")
        case 4:
         print("Thursday")
        case 5:
         print("Friday")
        case 6:
         print("Saturday")
        case 7:
         print("Sunday")

except ValueError:
    print("Enter a number from 1-7")
except Exception:
    print("Unknown error")



