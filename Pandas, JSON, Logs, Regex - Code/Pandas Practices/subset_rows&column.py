import pandas as pd

# Create sample DataFrame
data = {'A': [10, 20, 30, 40, 50],
        'B': [1, 2, 3, 4, 5],
        'C': ['X', 'Y', 'Z', 'W', 'V'],
        'D': [100, 200, 300, 400, 500]}

df = pd.DataFrame(data)

# Select rows 10-20
rows_10_to_20 = df.iloc[:2]
print("Rows 10-20:")
print(rows_10_to_20)
print()

# Select columns in positions 1, 2, and 3
selected_columns = df.iloc[:, [1, 2, 3]]
print("Selected columns:")
print(selected_columns)
print()

# Select all columns between 'x2' and 'x4' (inclusive)
selected_range_columns = df.loc[:, 'B':'D']
print("Selected range columns:")
print(selected_range_columns)
print()

# Select rows meeting logical condition and specific columns
condition = df['A'] > 20
selected_rows_and_columns = df.loc[condition, ['A', 'C']]
print("Selected rows and columns:")
print(selected_rows_and_columns)
print()

# Access a single value by index using df.iat
single_value_iat = df.iat[1, 2]
print("Single value (iat):", single_value_iat)
print()

# Access a single value by label using df.at
single_value_at = df.at[4, 'A']
print("Single value (at):", single_value_at)
