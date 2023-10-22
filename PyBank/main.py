import pandas as pd
from pathlib import Path
import locale


# First I imported the csv file using pandas
bank_csv = Path("Resources/budget_data.csv")
pd.set_option('display.max_rows', 100)
bank_df = pd.read_csv (bank_csv, encoding="utf-8")

# I counted the months using the count function in the date column
Total_months = bank_df["Date"].count()

# I then added al of the values from the column profits/losses using the 'sum' function and imported a currency in us dollars which is shown in the result at the end
Total_sum = bank_df["Profit/Losses"].sum()


# I used the function 'diff' the find all the differences between the months and then used those results to find the average using the 'mean' function.
row_changes= bank_df['Profit/Losses'].diff()
Average_Changes = row_changes.mean()
Average_Changes = round(Average_Changes,3)


# Here I used the 'max' funciont to find the greatest increase in the list 'row_changes' I created above
greatest_inc = row_changes.max()

# Then used 'loc' function to find the max values in the 'greatest_inc' list and used the 'values' function to only print the values I wanted from the list
inc_month= bank_df.loc[row_changes == greatest_inc, 'Date'].values[0]


#here I did the same as above but using the 'min' function instead of 'max'
Greatest_Dec= row_changes.min()
dec_month= bank_df.loc[row_changes == Greatest_Dec, 'Date'].values[0]


print('Financial Analysis')
print('-------------------')
print("Total Months : ", Total_months)
print("Total : ", locale.currency(Total_sum))
print("Average Change : ",'%',Average_Changes)
print("Greatest Increase in Profits : ", inc_month,'(', '$', greatest_inc,')')
print("Greatest decrease in Profits : ", dec_month, '(', '$', Greatest_Dec, ')')