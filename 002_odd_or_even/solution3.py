def check_number(num, divisor):
    if num % 4 == 0:
        print(f"{num} is a multiple of 4")
    elif num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

    if num % divisor == 0:
        print(f"{num} divides evenly by {divisor}")
    else:
        print(f"{num} does not divide evenly by {divisor}")


def main():
    try:
        num = int(input("Give me a number to check: "))
        divisor = int(input("Give me a number to divide by: "))
        check_number(num, divisor)
    except ValueError:
        print("Please enter valid integers.")


if __name__ == "__main__":
    main()