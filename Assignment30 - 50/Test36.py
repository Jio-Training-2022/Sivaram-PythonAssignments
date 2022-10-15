import numpy as np
import pandas as pd
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
print("Enter the entries in a single line (separated by space): ")
entries = list(map(int, input().split()))
matrix = np.array(entries).reshape(R, C)
arr = list(matrix)
df = pd.DataFrame(arr)
print(df)
print(type(df))