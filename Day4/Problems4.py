# 1) For any given integer array A ( read as input by the user ). How will you find the second largest element/value in the array? Write code for the same.

import math
arr = [34, 67, 12, 78, 54, 89, 15, 56]
# arr=[]       #if you want to enter the array elements from user
# n=int(input("Number of elements in array:"))
# for i in range(0,n):
#    l=int(input())
#    arr.append(l)
largest = -math.inf
slargest = -math.inf

for i in arr:
    if i >= largest:
        largest = i
        
for i in arr:
    if (i >= slargest) and (i < largest):
        slargest = i

print(largest)
print(slargest)
''' output
89
78
'''

# 2) Given an array nums ( read as input by the user), separate the odd and even numbers from the array and print them on separate lines.

arr = [34, 67, 12, 78, 54, 89, 15, 56]
# arr=[]       #if you want to enter the array elements from user
# n=int(input("Number of elements in array:"))
# for i in range(0,n):
#    l=int(input())
#    arr.append(l)
arr1=[]
arr2 =[]
for i in arr:
  if i%2 ==0 :
    arr1.append(i)
  else:
    arr2.append(i)
print(arr1)
print(arr2)

'''output
[34, 12, 78, 54, 56]
[67, 89, 15]
'''

# 3) Given a number A ( read as input ), find the sum of its digits.
def add_num(a,b):
        sum1=a+b
        print("Sum of two nos :", sum1)
a = int(input("First number :"))
b = int(input("Second number :"))
  
add_num(a,b)

'''output
First number :5
Second number :8
Sum of two nos :13'''
