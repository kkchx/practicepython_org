import random

def common_elements(list1, list2):
    # Use set intersection to find common elements without duplicates
    return list(set(list1) & set(list2))

# Generate two random lists of different sizes
list1 = random.sample(range(1, 20), 7)
list2 = random.sample(range(1, 20), 10)

print("List 1:", list1)
print("List 2:", list2)

common_elements_list = common_elements(list1, list2)
print("Common elements:", common_elements_list)