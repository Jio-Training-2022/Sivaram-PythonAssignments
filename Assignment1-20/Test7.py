from itertools import permutations 

input_statement = str(input(" Enter the statement : "))
permList = permutations(input_statement)

for perm in list(permList):
    print (''.join(perm))