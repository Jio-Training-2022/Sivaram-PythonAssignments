import pandas as pd
dataframe1 = pd.read_excel(r"C:\\Users\sivar\\OneDrive\Desktop\\Course\\Python\Sample.xlsx", sheet_name = 'Marks')
print(dataframe1.loc[:,"marks"])
print(dataframe1['marks'].mean())
