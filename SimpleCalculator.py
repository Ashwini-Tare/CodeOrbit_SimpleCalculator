#Project: Simple Calculator

print("welcome to the Simple Calculator")
print("Available Operations: +, -, *, /")

try:
    # Get two numbers from the user
    num1 = float(input("Enter the first number: "))

    # Get the second number from the user
    num2 = float(input("Enter the second number: "))

    # Get the operation from the user
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation based on the operation
    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        try:
            result = num1 / num2
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
    else:
        print("Invalid operation! Please enter a valid operation.")

except ValueError:
    print("Invalid input! Please enter numbers only.")     
