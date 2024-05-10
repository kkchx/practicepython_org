def find_divisors(num):
    divisorList = []
    for number in range(1, num + 1):
        if num % number == 0:
            divisorList.append(number)
    return divisorList


def main():
    try:
        num = int(input("Please choose a number to divide: "))
        find_divisors(num)
    except ValueError:
        print("Please enter a number.")


if __name__ == "__main__":
    main()