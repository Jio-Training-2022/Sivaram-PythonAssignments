#Write a program to find sum all Natural numbers from 1 to N where you have to take N as input from user
n = int(input('N : '))
c=0
for i in range (1,n+1):
  c= i+c
print("Summ of All natural numbers till N : ", c)
''' output
N : 15
Summ of All natural numbers till N : 120
'''

#Write a program to find simple interest on a principal amount A at interest rate of R for time period T. Take A, R and T as input from the user.
A = int(input('principal amount A : '))
R = float(input('interest rate R : '))
T = int(input('time period T : '))
print("Interest amt: ", (A*R*T)/100)

'''output
principal amount A : 10000
interest rate R : 5.5
time period T : 1
Interest amt:  550.0
'''
