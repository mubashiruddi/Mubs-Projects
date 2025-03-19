import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency,chi2
import matplotlib.pyplot as plt

# Load the data from Excel file
df = pd.read_excel("data.xlsx")

# Set Hypotheses
print(f'Ho: M = There is significant difference between the observed and expected frequencies.')
print(f'H1: M = There is no significant difference between the observed and expected frequencies.\n')

# Create the contingency table including the Variable column
contingency_table = df.pivot_table(index='Variable', values=['mail', 'Website', 'Both', 'None'])

# Perform Chi-Square Test
Chisquare = chi2_contingency(contingency_table)
table = pd.DataFrame(Chisquare.expected_freq, columns=['Mail', 'Website', 'Both', 'None'], index=contingency_table.index)

# Compute observed and expected totals
observeb_total = contingency_table.sum()
expected_total = table.sum()

# Print the results
if Chisquare.pvalue < 0.05:
    print(f"P-value amounts to {Chisquare.pvalue:.8f}  There is sufficient evidence to reject null hypothesis.")
else:
    print(f"P-value amounts to {Chisquare.pvalue:.8f} There is no sufficient evidence to reject null hypothesis.")

print(f"Degrees of Freedom: {Chisquare.dof}")
print("Expected Frequencies:")
print(table)

# Plot Observed vs Expected Frequency
categories = ['Mail', 'Website', 'Both', 'None']
bar_width = 0.15
index = np.arange(len(categories))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot observed frequencies
ax1.bar(index - bar_width / 2, observeb_total, bar_width, label='Observed')
# Plot expected frequencies
ax1.bar(index + bar_width / 2, expected_total, bar_width, label='Expected')

ax1.set_xlabel('Category')
ax1.set_ylabel('Frequency')
ax1.set_title('Observed vs Expected Frequencies with Chi-Square Test Results')
ax1.set_xticks(index)
ax1.set_xticklabels(categories)
ax1.legend()

# Chi-Square distribution plot with the calculated statistic
x = np.linspace(0, Chisquare.statistic, 100)
ax2.plot(x, chi2.pdf(x, Chisquare.dof), 'r-', lw=2, label='Chi-Square PDF')

# Shade the critical region
critical_value = chi2.ppf(1 - 0.05, Chisquare.dof)
ax2.fill_between(x, 0, chi2.pdf(x, Chisquare.dof), where=(x >= critical_value), color='gray', alpha=0.5, label=f'Critical Region (alpha = 0.05)')

# Plot the p-value point
p_value_x = Chisquare.statistic
p_value_y = chi2.pdf(p_value_x, Chisquare.dof)
ax2.plot(p_value_x, Chisquare.pvalue, 'bo', label=f'P-value: {Chisquare.pvalue:.8f}')

ax2.set_xlabel('Chi-Square Value')
ax2.set_ylabel('Probability Density')
ax2.set_title('Chi-Square Distribution')
ax2.legend()

# Display the plots
plt.tight_layout()
plt.show()
