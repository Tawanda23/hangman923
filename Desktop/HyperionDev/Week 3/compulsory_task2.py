import pandas as pd

# Create a DataFrame with balance.txt
df = pd.read_csv('balance.txt',sep=' ')
df

# Compare the average income based on ethnicity.
ethnic_income = df.groupby('Ethnicty')['Income'].mean().sort_values(ascending=False)
print("The average income based on ethnicity is: ", ethnic_income)

# On average, do married or single people have a higher balance?
single_balance = df[df['Marital_Status']== 'Single']['Balance'].mean()
married_balance = df[df['Marital_Status']== 'Married']['Balance'].mean()

if single_balance > married_balance:
    print("On average, single people have a higher balance")
else:
    print("On average, married people have a higher balance")

# What is the highest income in our dataset?
highest_income = df['Income'].max()

# What is the lowest income in our dataset?
lowest_income = df['Income'].min()

# How many cards do we have recorded in our dataset? (Hint: use sum())
df['Cards'].sum()

# How many females do we have information for vs how many males? (Hint: use count()For a list of all methods for computation of descriptive stats, explore the pandas documentation).
df['Gender'].value_counts()

