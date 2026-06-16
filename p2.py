"""
Given an array, return a new array with elements in reversed order.

Example
Input: [1, 2, 3, 4, 5] Output: [5, 4, 3, 2, 1]
"""

n=list(map(int,input("Enter the numbers:").split()))

n.reverse()
print(n)

#built-in
print(n[::-1])

#----------or-----------
#revesed approch
print(list(reversed(n)))


#--------------or---------------
#Two ppinter technique:-

left=0
right=len(n)-1

while left<right:
    n[left],n[right]=n[right],n[left]
    left+=1
    right-=1

print(n)

