def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True


def is_prime2(a):
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def get_integer():
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        print("please enter a number, try again")
        return get_integer()

if __name__ == "__main__":
    while True:
        number = get_integer()
        result = is_prime2(number)
        if result:
            print("prime number")
        else:
            print("not prime")
        choice = input("do you want to continue? y/n: ")
        if choice == "n":
            break