"""Given an array of integers, find and return the largest element.

Example
Input: [3, 1, 7, 2, 9, 4] Output: 9
"""


n=list(map(int,input("Enter the numbers:").split()))

max_val=n[0]
for i in range(1,len(n)):
    if n[i]>max_val:
        max_val=n[i]
print(max_val)