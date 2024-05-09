import random

def common_elements(list1, list2):
    #TODO rewrite the logic using for loop and if
    list1 = list(set(list1))
    list2 = list(set(list2))
    result = []

    for i in range(0,len(list1)):
        if list1[i] in list2:
            result.append(list1[i])
    return result

# Generate two random lists of different sizes using random.randint
list1_size = random.randint(5, 10)
list2_size = random.randint(5, 10)

list1 = [random.randint(1, 20) for _ in range(list1_size)]
list2 = [random.randint(1, 20) for _ in range(list2_size)]

print("List 1:", list1)
print("List 2:", list2)

result = common_elements(list1, list2)
print("Common elements:", result)