def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    try:
        number = int(input("Enter a number: "))
        if number <= 0:
            print("Please enter a positive integer.")
            return
        divisors = find_divisors(number)
        print(f"The divisors of {number} are: {divisors}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()