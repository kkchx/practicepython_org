def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


def remove_duplicates_check(input_list):
    unique_list = []
    for item in input_list:
        if input_list.count(item) > 1:
            continue
        unique_list.append(item)
    return unique_list
