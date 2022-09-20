#FizzBuzz Problem 3, 5 and (3,5) Divisibility check 
for N in range(1,101):
  if N%3 ==0 and N%5 ==0:
    print('fizzbuzz',end = ' ')
  elif N%5 ==0:
    print('fizz',end = ' ')
  elif N%3 ==0 :
    print('buzz',end = ' ')
  else:
    print(N, end = ' ')

''' Output
1 2 buzz 4 fizz buzz 7 8 buzz fizz 11 buzz 13 14 fizzbuzz 16 17 buzz 19 fizz buzz 22 23 buzz fizz 26 buzz 28 29 fizzbuzz 31 32 buzz 34 fizz buzz 37 38 buzz fizz 41 buzz 43 44 fizzbuzz 46 47 buzz 49 fizz buzz 52 53 buzz fizz 56 buzz 58 59 fizzbuzz 61 62 buzz 64 fizz buzz 67 68 buzz fizz 71 buzz 73 74 fizzbuzz 76 77 buzz 79 fizz buzz 82 83 buzz fizz 86 buzz 88 89 fizzbuzz 91 92 buzz 94 fizz buzz 97 98 buzz fizz '''
    
    
