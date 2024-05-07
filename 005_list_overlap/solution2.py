import random

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Generate two random lists of different sizes using random.randint
list1_size = random.randint(5, 10)
list2_size = random.randint(5, 10)

list1 = [random.randint(1, 20) for _ in range(list1_size)]
list2 = [random.randint(1, 20) for _ in range(list2_size)]

print("List 1:", list1)
print("List 2:", list2)

common_elements_list = common_elements(list1, list2)
print("Common elements:", common_elements_list)