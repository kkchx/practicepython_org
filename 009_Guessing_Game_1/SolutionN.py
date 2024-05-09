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
        return 1 #


if "__name__" == "__main__":

