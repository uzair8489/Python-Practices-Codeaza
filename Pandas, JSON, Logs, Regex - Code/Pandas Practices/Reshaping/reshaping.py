import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Uzair', 'Ahad'],
    'Maths_Score': [90, 80],
    'Science_Score': [95, 85]
}

df = pd.DataFrame(data)

# Melt the DataFrame (Spread rows into columns)
print("\nMelted Form:")
melted_df = df.melt(id_vars='Name', var_name='Subject', value_name='Score')
print(melted_df)

print("\nSorted Form:")
sorted_df = df.sort_values(by='Maths_Score')
print(sorted_df)

print("\nRenamed Scores Columns:")
renamed_df = df.rename(columns = {'Maths_Score':'Maths', 'Science_Score':'Science'})
print(renamed_df)

