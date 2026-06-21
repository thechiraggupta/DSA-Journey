"""" Return the second largest unique element in the array. Assume at least 2 distinct values exist.

Example

Input: [10, 20, 4, 45, 99] Output: 45"""

n = list(map(int, input("Enter the numbers: ").split()))

first = second = float('-inf')   # negative infinity as starting point

for num in n:
    if num > first:
        second = first           # old max becomes second
        first = num              # new max
    elif num > second and num != first:  # bigger than second but not a duplicate
        second = num

print(second)
