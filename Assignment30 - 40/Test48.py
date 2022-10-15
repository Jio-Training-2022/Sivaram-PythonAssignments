from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(r'C:\Users\sivar\OneDrive\Desktop\Course\Python\Sample'):
    f.extend(filenames)
    break
    
print(f)