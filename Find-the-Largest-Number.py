#: Write a function that accepts three numbers and returns the largest one without using the built-in max() function.
def largest(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print("The largest number is:", largest(a, b, c))