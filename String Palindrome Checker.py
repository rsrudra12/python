# Write a function that checks whether a given string is a palindrome.
# It ignores capitalization and spaces/punctuation.
def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
