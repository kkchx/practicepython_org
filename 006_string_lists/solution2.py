def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

try:
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
except Exception as e:
    print("An error occurred:", e)