def find_largest(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

# Example usage:
num1 = 10
num2 = 5
num3 = 8
largest = find_largest(num1, num2, num3)
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")