#Write a program that checks if two strings are anagrams of each other (contain the exact same letters in a different order, like "listen" and "silent").
def anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)

# Test the function
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = anagram(str1, str2)

if result:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
