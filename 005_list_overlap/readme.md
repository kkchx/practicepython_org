## List Overlaps
This Python script is designed to find common elements between two lists using the `common_elements()`<br>
function. It utilizes set intersection to efficiently identify common elements without duplicates.

<details>
<summary><b> Solutions</b></summary>

1. Basic function <br>
2. Added random.randint
</details>

<details>
<summary><b> Example</b></summary>

import random <br>
def common_elements(list1, list2): <br>
    # Use set intersection to find common elements without duplicates <br>
    return list(set(list1) & set(list2)) 

# Generate two random lists of different sizes
list1 = random.sample(range(1, 20), 7) <br>
list2 = random.sample(range(1, 20), 10)

print("List 1:", list1) <br>
print("List 2:", list2)

common_elements_list = common_elements(list1, list2) <br>
print("Common elements:", common_elements_list)

List 1: [2, 6, 7, 11, 5, 16, 10] <br>
List 2: [8, 7, 12, 14, 18, 9, 6, 1, 19, 4] <br>
Common elements: [6, 7]
</details>

<details>
<summary><b> How its Works</b></summary>

1. Two random lists, list1 and list2, of different sizes are generated using the random.sample() function. <br>
2. The common_elements() function takes these lists as input and returns a list containing their common elements. <br>
3. Inside the common_elements() function, set intersection (&) is used between the two lists to find common elements efficiently. <br>
4. The resulting list of common elements is printed to the console.
</details>