import pandas as pd
dataframe1 = pd.read_excel(r"C:\\Users\sivar\\OneDrive\Desktop\\Course\\Python\Sample1.xlsx")
print(dataframe1['Numbers'].mean())
print(dataframe1['Numbers'].median())
print(dataframe1['Numbers'].mode())