f = open("readme.xlsx", "a")
f.write("Now the file has more content!")
f = open("readme.xlsx", "r")
print(f.read())    