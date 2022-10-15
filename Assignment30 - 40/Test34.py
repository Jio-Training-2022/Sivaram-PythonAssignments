import pandas as pd
f = open("Arrayfile.txt", "r")
c = f.read()
c = c.split(' ')
ser = pd.DataFrame(c)
print(ser)