"""" Return the second largest unique element in the array. Assume at least 2 distinct values exist.

Example

Input: [10, 20, 4, 45, 99] Output: 45"""

n=list(map(int,input("Enter the number:").split()))

n.sort()
print(n[-2])
