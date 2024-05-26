def get_integer():
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        print("please enter a number, try again")
        return get_integer()

def find_max_2(numbers):
    max = numbers[0]
    for num in numbers[1:]:
        if num > max:
            max = num
    return max

if __name__ == "__main__":
    numbers = []
    print("Please provide 5 numbers to find the max:")

    for i in range(5):
        numbers.append(get_integer())

    max = find_max_2(numbers)
    print(f"The max is {max}")
