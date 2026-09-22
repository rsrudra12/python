# Ask the user for two numbers and an operator (+, -, *, /), then print the calculated result.
a=float(input("enter first number:  "))
b=float(input("enter second number:  "))
operator=input("enter operator (+, -, *, /):  ")
if operator == "+":
    print(f"addition: {a+b}")
elif operator == "-":
    print(f"subtraction: {a-b}")
elif operator == "*":
    print(f"multiplication: {a*b}")
elif operator == "/":
    print(f"division: {a/b}" if b != 0 else "Error: Division by zero")
else:
    print("Invalid operator")