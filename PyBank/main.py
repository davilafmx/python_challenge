
import pandas as pd
from pathlib import Path
import locale

bank_csv = Path("Resources/budget_data.csv")
bank_df = pd.read_csv (bank_csv, encoding="utf-8")
Total_months = bank_df["Date"].count()
Total_months
print("Total Months : ", Total_months)
Total_sum = bank_df["Profit/Losses"].sum()
locale.setlocale( locale.LC_ALL, '' )
'English_United States.1252'
locale.currency(Total_sum)
print("Total Sum : ", locale.currency(Total_sum))

