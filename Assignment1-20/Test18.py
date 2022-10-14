
print("Enter a String: ", end="")
text = input()
textlength = len(text)
sum = 0
for char in text:
    ascii = ord(char)+10
    charac = chr(ascii)
    print(charac, "\t", ascii)