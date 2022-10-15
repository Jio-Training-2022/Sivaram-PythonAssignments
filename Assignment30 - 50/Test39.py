import pandas as pd
import numpy as np
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
print("Enter the entries in a single line (separated by space): ")
entries = list(map(int, input().split()))
print(entries)
matrix = np.array(entries).reshape(R, C)
arr = list(matrix)
df = pd.DataFrame(arr)
with pd.ExcelWriter("file_39.xlsx") as writer:

    df.to_excel(writer, sheet_name="data1", index=False)
    df.to_excel(writer, sheet_name="data2", index=False)
    df.to_excel(writer, sheet_name="data3", index=False)