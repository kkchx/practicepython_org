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

def main(list):
    today = datetime.now().year
    res_year = 100 - list[1] + list[2]
    return res_year

if __name__ == "__main__":
    user_entry = []
    data = user_input(user_entry)
    res_year = main(data)
    print(f"Hey {data[0]}! You will turn 100 years old in {res_year}.")