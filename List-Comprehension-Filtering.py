#Given a list of integers, use a single line of list comprehension to create a new list containing only the squares of the even numbers
A = input("Enter a list of integers separated by commas: ")
# Convert the input string to a list of integers
A = [int(x) for x in A.split(",")]
# Use list comprehension to create a new list containing only the squares of the even numbers
B = [x**2 for x in A if x % 2 == 0]
print("Squares of even numbers:", B)