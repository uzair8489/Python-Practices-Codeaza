import pandas as pd

# Create DataFrame
data = {'Name': ['Uzair', 'Ahad', 'Sufyan', 'Afaq', 'Afaq'],
        'Age': [25, 30, 20, 25, 25],
        'Salary': [5000, 7000, 4000, 5000, 5000]}

df = pd.DataFrame(data)

# Filter columns using regex pattern
filtered_cols = df.filter(regex='^N')
print("Filtered columns:")
print(filtered_cols)
print()

# Query the DataFrame using a condition
query_result = df.query('Age >= 25 and Salary < 6000')
print("Query result:")
print(query_result)
print()
