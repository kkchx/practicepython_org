def user_input():
    try:
        name = str(input("Enter your name: "))
        age = int(input("Enter your age: "))
        current_year = int(input("Enter the current year: "))
        return name, age, current_year
    except ValueError:
        print("Please enter numbers for age and current year.")
        return None, None, None

def main():
    name, age, current_year = user_input()
    if name is not None and age is not None and current_year is not None:
        res_year = 100 - age + current_year
        print(f"Hey {name}! You will turn 100 years old in {res_year}.")
    else:
        print("Unable to calculate. Please try again.")

main()