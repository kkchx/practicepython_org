TEST_LIST = [0, 1, 4, 5, 6, 7, 9]
TEST_LIST2 = []
TEST_LIST3 = [1, 2, 5, 7]

def first_last(list):
    if len(list) > 0:
        res_list = []
        res_list.append(list[0])
        res_list.append(list[-1])
        print(res_list)
        return res_list
    else:
        print("the list is empty.")


if __name__ == '__main__':
    list = TEST_LIST3
    first_last(list)