#Hackerrank problems:

#Problem 1) Hello world problem Exercise 

Store  = "Hello, World!"
  print(Store)

#Problem 2) Printing Without using any string methods till n

n = int(input())
  for i in range (n):
    print(i+1, end='')
        
# Problem 3)
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

def add_num(a,b):
        sum1=a+b
        print(sum1)

def diff(a,b):
        diff=a-b
        print(diff)
    
def product(a,b):
        product=a*b
        print(product)

a = int(input())
b = int(input())
  
add_num(a,b)
diff(a,b)
product(a,b)
