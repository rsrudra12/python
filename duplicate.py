def duplicate(a):
    unique = []
    for i in a:
        if i not in unique:
            unique.append(i)    
    return unique
a = input("Enter a list of elements: ")
a = a.split(",")
print("List with duplicates:", a)   
b=duplicate(a)
print("List without duplicates:", b)