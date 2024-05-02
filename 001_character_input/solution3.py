from datetime import datetime
def user_input(data):
    try:
        data.append(str(input("Enter your name: ")))
        data.append(int(input("Enter your age: ")))
        data.append(datetime.now().year)
        return data
    except ValueError:
        print("Please enter numbers for age and current year.")
        data = []
        return user_input(data)

def main():
    today = datetime.now().year
    user_entry = []
    user_entry = user_input(user_entry)
    res_year = 100 - user_entry[1] + user_entry[2]
    print(f"Hey {user_entry[0]}! You will turn 100 years old in {res_year}.")

main()