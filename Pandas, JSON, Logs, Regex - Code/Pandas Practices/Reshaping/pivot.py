import pandas as pd

# Create a sample DataFrame
data = {
    'City': ['London', 'Paris', 'Berlin', 'Paris', 'Berlin'],
    'Year': [2019, 2019, 2020, 2020, 2021],
    'Population': [8900000, 2141000, 3769000, 2271000, 3890000]
}


df = pd.DataFrame(data)
# Perform pivot operation
print("Pivoted Data:")
pivot_df = df.pivot(index='City', columns='Year', values='Population')
print(pivot_df, '\n')




