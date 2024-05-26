def remove_duplicates(input_list):
    return list(set(input_list))

# """def remove_duplicates_check(input_list):
#     count_dict = {}
#     for item in input_list:
#         count_dict[item] = count_dict.get(item, 0) + 1
#     return [item for item, count in count_dict.items() if count == 1]"""

def remove_duplicates_no_sort(input_list):
    result = []
    for item in input_list:
        if item not in result:
            result.append(item)
    return result

def remove_duplicates_no_sort2(input_list):
    result = []
    for i in range(0,len(input_list)):
        if input_list[i] not in result:
            result.append(input_list[i])
    return result
def main():
    # Sample input data
    input_list = [5, 4, 3, 3, 4, 2, 1]

    # Remove duplicates using the first function
    unique_list_1 = remove_duplicates(input_list)
    print(input_list)
    result = remove_duplicates_no_sort(input_list)
    result2 = remove_duplicates_no_sort2(input_list)
    print("Unique list using remove_duplicates:", result2)

    # Remove duplicates using the second function
   # unique_list_2 = remove_duplicates_check(input_list)
   # print("Unique list using remove_duplicates_check:", unique_list_2)

if __name__ == "__main__":
    main()
