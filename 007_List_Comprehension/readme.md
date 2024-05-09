## List Sorter Even Number
This simple Python script filters a list to extract only the even numbers.

<details>
<summary><b> Solutions</b></summary>

1. Basic yet effective one line code list comprehension
</details>


<details>
<summary><b> Usage</b></summary>

To use this script, follow these steps:
1. Ensure you have Python installed on your system.
2. Copy the code into a Python file or script.
3. Call the `list_sorter` function and pass your list as an argument.
4. The function will return a new list with only the even numbers.
</details>


<details>
<summary><b> Example</b></summary>

```python
from list_sorter import list_sorter

if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Source list: {test_list}")
    print(f"Result list: {list_sorter(test_list)}")
```
</details>


<details>
<summary><b> How its Works</b></summary>

- The list_sorter function iterates through each element of the input list.
- It checks if each element is even (i.e., divisible by 2).
- If the element is even, it is added to a new list called res_list.
- After iterating through all elements, the function returns the res_list containing only the even numbers.
</details>