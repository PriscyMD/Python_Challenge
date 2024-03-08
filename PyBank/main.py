import pandas as pd

#df = pd.read_csv("C:/Users/Priscy/Desktop/GitHubRepository/Python_Challenge/PyBank/Resources.csv")
#df.head()
# Create a DataFrame from the provided data
df = pd.read_csv("C:/Users/Priscy/Desktop/GitHubRepository/Python_Challenge/PyBank/Resources.csv")

#Total Months
Totalmonths = df["Date"].count()

#net_amount = df["Profit/Losses"].sum()
#print(f"Total meses: {months}/n/nTotal: ${net_amount}")
#Total Profit/Losses
Total = df["Profit/Losses"].sum()

#Average Changes
#df["Cambios"] = df["Profit/Losses"].diff()
#df["Cambios"].mean()
#df["Profit/Losses"].max()
Average = df["Cambios"] = df["Profit/Losses"].diff()
Average = df["Cambios"].mean()

#Increase Profits
#print(f"Total meses: {gratest_increase_date.values} ${gratest_increase_amount.values}")
gratest_increase = df[df["Cambios"].isin([ df["Cambios"].max() ])][["Date", "Cambios"]]
gratest_increase_date = gratest_increase["Date"]
gratest_increase_amount = gratest_increase["Cambios"]

#Decrease Profits
#gratest_decrease = df["Profit/Losses"].diff().min()
#gratest_decrease
gratest_decrease = df[df["Cambios"].isin([ df["Cambios"].min() ])][["Date", "Cambios"]]
gratest_decrease_date = gratest_decrease["Date"]
gratest_decrease_amount = gratest_decrease["Cambios"]

#Results
print(f'''
Financial Analytics:
      
--------------------------------------------------
      
Total months {Totalmonths}

Total: ${Total}

Average Change: ${Average}

Greatest Increase in profits: {gratest_increase_date.values} {gratest_increase_amount.values}

Greatest Decrease in profits: {gratest_decrease_date.values} {gratest_increase_amount.values}
''')

