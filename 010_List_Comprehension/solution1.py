def intersection(list1, list2):
    list1 = list(set(list1))
    list2 = list(set(list2))
    #TODO test shorter and longer lists
    res_list = [item for item in list1 if item in list2]
    return res_list


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [1, 2, 3, 3]
    print(f"List 1 {a}\nList 2 {b}\nIntersection {intersection(a,b)}")