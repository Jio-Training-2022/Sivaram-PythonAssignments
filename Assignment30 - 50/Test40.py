import pandas as pd
sheet_id = '1hL2jBxWn9jJ9T8PunJR44oiwFgBF72juUKWAURsc3TU'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
print(df)
