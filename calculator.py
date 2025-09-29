

def calculator():
    print("===== SIMPLE CALCULATOR =====")
    print("Operations: +  -  *  /")

    while True:
        try:

            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))


            operation = input("Enter the operation (+, -, *, /): ").strip()


            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print(" Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("⚠ Invalid operation! Please choose +, -, *, or /.")
                continue


            print(f" Result: {num1} {operation} {num2} = {result}")

        except ValueError:
            print("⚠ Error: Please enter valid numbers.")


        choice = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
        if choice != 'y':
            print(" Thank you for using the calculator. Goodbye!")
            break


calculator()
