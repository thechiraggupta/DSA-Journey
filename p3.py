""" Given an array, return True if it is sorted in non-decreasing order, else False.

Example

Input: [1, 2, 2, 5, 9] Output: True Input: [3, 1, 4] Output: False"""

n=list(map(int,input("Enter the numbers:").split()))

is_sorted=True
for i in range (len(n)):
    if n[i]>n[i+1]:
        is_sorted=False
        break
print(is_sorted)