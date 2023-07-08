import pandas as pd

# Create DataFrame
data = {'Name': ['Uzair', 'Ahad', 'Sufyan', 'Afaq', 'Afaq'],
        'Age': [25, 30, 20, 25, 25],
        'Salary': [5000, 7000, 4000, 5000, 5000]}

df = pd.DataFrame(data)

# Remove duplicate rows based on all columns
df_no_duplicates = df.drop_duplicates()
print("DataFrame without duplicates:")
print(df_no_duplicates)
print()

# Randomly select 50% of the rows
df_sample_frac = df.sample(frac=0.5)
print("Randomly selected 50% of the rows:")
print(df_sample_frac)
print()

# Randomly select 2 rows
df_sample_n = df.sample(n=2)
print("Randomly selected 2 rows:")
print(df_sample_n)
print()

# Select and order the top 2 entries based on Salary
df_top_n = df.nlargest(2, 'Salary')
print("Top 2 entries based on Salary:")
print(df_top_n)
print()

# Select and order the bottom 1 entry based on Salary
df_bottom_n = df.nsmallest(1, 'Salary')
print("Bottom 1 entry based on Salary:")
print(df_bottom_n)
print()

# Select the first 2 rows
df_first_n = df.head(2)
print("First 2 rows:")
print(df_first_n)
print()

# Select the last 2 rows
df_last_n = df.tail(2)
print("Last 2 rows:")
print(df_last_n)
print()
