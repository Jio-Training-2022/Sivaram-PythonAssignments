for N in range(1,101):
  if N%3 ==0 and N%5 ==0:
    print('fizzbuzz',end = ' ')
  elif N%5 ==0:
    print('fizz',end = ' ')
  elif N%3 ==0 :
    print('buzz',end = ' ')
  else:
    print(N, end = ' ')