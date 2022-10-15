import numpy as np
import pandas as pd
Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
print("Enter the entries in a single line (separated by space): ")
entries = list(map(int, input().split()))
matrix = np.array(entries).reshape(Row, Column)
arr = list(matrix)
df = pd.DataFrame(arr)
df.to_csv('file_37.csv')