try:
    num_1 = int(input("Enter first number:"))
    num_2 = int(input("Enter second number:"))

    if num_1 == num_2:
        print("Numbers are equal")
    else:
         if num_1 < num_2:
            print(f"Numbers in ascending order: {num_1}, {num_2}.")
         else:
            print(f"Numbers in ascending order: {num_2}, {num_1}.")

except ValueError:
    print("Enter the numbers")
except Exception as e:
    import logging
    logging.error(f"Unknown error: {e}")