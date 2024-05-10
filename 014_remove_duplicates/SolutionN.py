def remove_duplicates(input_list):
    return list(set(input_list))

def remove_duplicates_check(input_list):
    count_dict = {}
    for item in input_list:
        count_dict[item] = count_dict.get(item, 0) + 1
    return [item for item, count in count_dict.items() if count == 1]

def main():
    # Sample input data
    input_list = [1, 2, 2, 3, 4, 4, 5]

    # Remove duplicates using the first function
    unique_list_1 = remove_duplicates(input_list)
    print("Unique list using remove_duplicates:", unique_list_1)

    # Remove duplicates using the second function
    unique_list_2 = remove_duplicates_check(input_list)
    print("Unique list using remove_duplicates_check:", unique_list_2)

if __name__ == "__main__":
    main()
