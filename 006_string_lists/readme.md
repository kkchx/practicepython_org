## String lists
This Python script checks whether a given string is a palindrome or not. A palindrome is a word, <br>
phrase, number, or other sequence of characters that reads the same forward and backward.

<details>
<summary><b> Solutions</b></summary>

1. Most basic solutions without error control <br>
2. Added function and error control
</details>


<details>
<summary><b> Example</b></summary>

Ask the user for input <br>
```python
user_input = input("Enter a string: ")

# Check if the input string is a palindrome
if user_input == user_input[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
```
</details>

<details>
<summary><b> Example Usage</b></summary>

Enter a string: radar <br>
The string is a palindrome.

Enter a string: hello <br>
The string is not a palindrome.

</details>
<details>
<summary><b> How its Works</b></summary>

- The script prompts the user to input a string using the input() function. <br>
- It then checks whether the input string is a palindrome or not by comparing it with its reverse using slicing ([::-1]). <br>
- If the input string is the same as its reverse, it prints "The string is a palindrome."; otherwise, it prints "The string is not a palindrome."
</details>