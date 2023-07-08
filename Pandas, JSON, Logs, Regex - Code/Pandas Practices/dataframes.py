import pandas as pd

# Creating a dictionary including the data
data = {'Name': ['Uzair', 'Ahad', 'Sufyan'],
        'Age': [25, 30, 35],
        'City': ['Lahore', 'Multan', 'Sahiwal']}

# Passing the data into dataframe for representation
df = pd.DataFrame(data)
print(df)

"""
In this example, i created a DataFrame using a Python dictionary. When we pass the dictionary to the pd.DataFrame() function, 
and it creates a DataFrame with three columns: 'Name', 'Age', and 'City'. The output shows the DataFrame with the provided data.

"""
