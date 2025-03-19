import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load data from CSV file
df = pd.read_excel("data.xlsx")

# Restructure the data (assuming the first column is 'Variable')
df.set_index('Variable', inplace=True)

# Compute the correlation matrix
correlation_matrix = df[['mail', 'Website', 'Both', 'None']].corr()

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Perform hypothesis test on correlation coefficients
methods = ['mail', 'Website', 'Both', 'None']
p_values = pd.DataFrame(index=methods, columns=methods)

for i in range(len(methods)):
    for j in range(i + 1, len(methods)):
        corr, p_value = pearsonr(df[methods[i]], df[methods[j]])
        p_values.loc[methods[i], methods[j]] = p_value
        p_values.loc[methods[j], methods[i]] = p_value

# Print the p-values
print("\nP-values for Correlation Coefficients:")
print(p_values)

# Define the significance level (alpha)
alpha = 0.05

# Interpret the p-values
for i in range(len(methods)):
    for j in range(i + 1, len(methods)):
        if p_values.loc[methods[i], methods[j]] < alpha:
            print(f"\nReject the null hypothesis for correlation between {methods[i]} and {methods[j]}.")
            print(f"There is significant evidence to suggest that there is a correlation between {methods[i]} and {methods[j]}.")
        else:
            print(f"\nFail to reject the null hypothesis for correlation between {methods[i]} and {methods[j]}.")
            print(f"There is no significant evidence to suggest that there is a correlation between {methods[i]} and {methods[j]}.")

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()