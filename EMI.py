#Monthly EMI calculator
p = float(input("principal amount : "))
R = float(input("interest rate R : "))
n = int(input("time period T in months : " ))

r = R/(12*100)

EMI = p * r * ((1+r)**n)/((1+r)**n - 1)

print("Monthly EMI = ", EMI)

''' Output
principal amount : 10000
interest rate R : 5.5
time period T in months : 2
Monthly EMI =  5034.40119864197
'''
