
print("Enter a String: ", end="")
text = input()
textlength = len(text)
sum = 0
for char in text:
    ascii = ord(char)+10
    sum = sum + ascii
    print(char, "\t", ascii)
print("sum of ascii values of all characters : ", sum)
    
