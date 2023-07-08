import pandas as pd

# Create a sample DataFrame
data = {'w': ['A', 'B', 'C', 'A', 'B', 'A']}
df = pd.DataFrame(data)

# Count number of rows with each unique value of 'w'
value_counts = df['w'].value_counts()
print("value count in", value_counts)
print()

# Get the number of rows in the DataFrame
num_rows = len(df)
print("Rows Count: ",num_rows)
print()

# Get the shape of the DataFrame (number of rows, number of columns)
shape = df.shape
print("Shape:",shape)
print()

# Get the number of distinct values in column 'w'
num_unique_values = df['w'].nunique()
print("Distinct Values: ",num_unique_values)
print()

# Get basic descriptive statistics for each column
description = df.describe()
print("Description Of Data in",description)
print()
