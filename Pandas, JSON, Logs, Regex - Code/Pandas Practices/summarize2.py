import pandas as pd

# Create a sample DataFrame
data = {'x': [1, 2, 3, 4, 5],
        'y': [6, 7, 8, 9, 10],
        'z': [11, 12, 13, 14, 15]}
df = pd.DataFrame(data)

# Sum of values in each column
sum_values = df.sum()
print("Sum of values:")
print(sum_values)

# Count non-NA/null values in each column
count_values = df.count()
print("Count of non-null values:")
print(count_values)

# Median value of each column
median_values = df.median()
print("Median values:")
print(median_values)

# Quantiles (25th and 75th percentiles) of each column
quantiles = df.quantile([0.25, 0.75])
print("Quantiles (25th and 75th percentiles):")
print(quantiles)

# Apply a function to each column
square_values = df.apply(lambda x: x**2)
print("Squared values:")
print(square_values)

# Minimum value in each column
min_values = df.min()
print("Minimum values:")
print(min_values)

# Maximum value in each column
max_values = df.max()
print("Maximum values:")
print(max_values)

# Mean value of each column
mean_values = df.mean()
print("Mean values:")
print(mean_values)

# Variance of each column
var_values = df.var()
print("Variance values:")
print(var_values)

# Standard deviation of each column
std_values = df.std()
print("Standard deviation values:")
print(std_values)
