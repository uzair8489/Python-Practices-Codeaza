import pandas as pd

# Create a sample DataFrame
data = {
    'Value': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Shift values by 1
shifted = df['Value'].shift(1)
print("Shifted values:")
print(shifted)

# Calculate cumulative sum
cumulative_sum = df['Value'].cumsum()
print("\nCumulative sum:")
print(cumulative_sum)

# Calculate cumulative maximum
cumulative_max = df['Value'].cummax()
print("\nCumulative maximum:")
print(cumulative_max)

# Calculate cumulative minimum
cumulative_min = df['Value'].cummin()
print("\nCumulative minimum:")
print(cumulative_min)

# Calculate cumulative product
cumulative_prod = df['Value'].cumprod()
print("\nCumulative product:")
print(cumulative_prod)
