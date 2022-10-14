import pandas as pd
dataframe1 = pd.read_excel(r"C:\\Users\sivar\\OneDrive\Desktop\\Course\\Python\Sample.xlsx", sheet_name = 'Names',)
Name = str(input("Enter the name "))
print(dataframe1[dataframe1['Names'] ==  Name])
