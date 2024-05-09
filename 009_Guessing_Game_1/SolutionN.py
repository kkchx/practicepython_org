import random

def get_integer():
    try:
        res = int(input("Please enter a number: "))
        return res
    except:
        print("Not a valid number, please try again")
        return get_integer()

def compare(a, b):
    if a == b:
        return 0 # win
    elif a > b:
        return -1 # too low
    else:
        return 1


if __name__ == "__main__":
    while True:
        computer_choice = random.randint(0, 20)
        while True:
            user_choice = get_integer()
            result = compare(computer_choice, user_choice)
            if result == 0:
                print("You win")
                break
            elif result == -1:
                print("Too low")
            else:
                print("Too high")
        choice = input("do you want to continue? y/n: ")
        if choice == "n":
            break