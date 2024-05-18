def get_integer():
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        print("please enter a number, try again")
        return get_integer()

def find_largest(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

def find_largest_2(numbers):
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

if __name__ == "__main__":
    numbers = []
    print("Please provide 3 numbers to find the largest:")

    for i in range (3):
        numbers.append(get_integer())

    largest = find_largest_2(numbers)
    print(f"The largest is {largest}")
