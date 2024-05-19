import random


def guess_number():
    print("Welcome to the Higher or Lower game!")
    print("Think of a number between 1 and 100 and I'll try to guess it.")

    lower_bound = 1
    upper_bound = 100
    attempts = 0

    while True:
        guess = random.randint(lower_bound, upper_bound)
        print(f"Is your number {guess}?")
        response = input("Enter 'higher', 'lower', or 'correct': ").lower()

        if response == 'higher':
            lower_bound = guess + 1
        elif response == 'lower':
            upper_bound = guess - 1
        elif response == 'correct':
            print("Great! I guessed your number in {} attempts.".format(attempts))
            break
        else:
            print("Invalid input. Please enter 'higher', 'lower', or 'correct'.")

        attempts += 1


# Start the game
guess_number()
