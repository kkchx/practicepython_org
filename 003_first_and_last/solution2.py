TEST_LIST = [0, 1, 4, 5, 6, 7, 9]
TEST_LIST2 = []
TEST_LIST3 = [1, 2, 5, 7]

def extract_first_and_last(lst):
    if lst:  # Checks if the list is not empty
        return [lst[0], lst[-1]]
    else:
        return None  # Returning None for an empty list


if __name__ == '__main__':
    my_list = TEST_LIST3
    result = extract_first_and_last(my_list)
    if result:
        print(result)
    else:
        print("The list is empty.")