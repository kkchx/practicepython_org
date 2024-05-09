def list_sorter(list):
    res_list = [x for x in list if x%2==0]
    return res_list

if __name__ == '__main__':
    test_list = [1,2,3,4,5,6,7,8,9]
    print(f"Source list: {test_list}\nResult list: {list_sorter(test_list)}")