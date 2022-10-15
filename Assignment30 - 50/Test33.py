import pandas as pd
f = open("Arrayfile.txt", "r")
c = f.read()
c = c.split(' ')
df = pd.DataFrame(c)
print(df)