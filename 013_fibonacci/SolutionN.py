def fibonacci(limit):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= limit:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

def main():
    limit = int(input("Enter the limit for the Fibonacci sequence: "))
    sequence = fibonacci(limit)
    print("Fibonacci sequence up to", limit, "is:", sequence)

if __name__ == "__main__":
    main()