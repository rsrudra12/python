#Write a function that takes a list and returns a new list containing only the unique elements without using the built-in set() function.
def remove_duplicates(a):
    unique_list = []
    for item in a:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
A=input("Enter a list of elements: ")
# Convert the input string to a list
A = A.split(",")
print("List with duplicates:", A)
B = remove_duplicates(A)
print("List without duplicates:", B)