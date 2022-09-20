N=int(input())
for i in range (N+1):
  print(i, end = " ")

'''output

23
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 
'''

lst = []
n = int(input("Enter multiplication table number size : "))
for i in range(1, n+1):
   lst.append(i)
table_number = int(input("Enter the table number: "))
table = [elem*table_number for elem in lst]
print(table)

'''output
Enter multiplication table number size : 12
Enter the table number: 9
[9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108]
'''
