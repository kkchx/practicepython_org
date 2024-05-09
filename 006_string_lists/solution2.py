def is_palindrome(string_to_check):
    result = 1

    for i in range(0,int(len(string_to_check)/2)):
        if string_to_check[i] != string_to_check[len(string_to_check)-i-1]:
            result -= 1
            break

    return result


if __name__ == "__main__":
    while True:
        try:
            string_to_check = input("Input a string to check\n")
            if is_palindrome(string_to_check) == 1:
                print("It's a Palindrome")
            else:
                print("It's Not a Palindrome")
        except Exception as e:
            print("An error occurred:", e)