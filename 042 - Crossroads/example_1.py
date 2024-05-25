def main():
    print("Welcome to the Adventure Game!")
    name = input("What is your name? ")
    print(f"Hello, {name}! Let's begin your adventure.")

    print("You find yourself standing at a crossroads.")
    choice = input("Do you go left or right? (left/right) ").lower()

    if choice == "left":
        print("You encounter a ferocious dragon!")
        fight_or_run = input("Do you want to fight or run? (fight/run) ").lower()
        if fight_or_run == "fight":
            print("You bravely attack the dragon but are defeated. Game over!")
        elif fight_or_run == "run":
            print("You run away and live to fight another day. You win!")
        else:
            print("Invalid choice. Please try again.")
    elif choice == "right":
        print("You find a treasure chest!")
        print("Congratulations! You win!")
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
