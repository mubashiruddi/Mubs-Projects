import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as stats
from scipy.stats import mannwhitneyu,norm,binom
import matplotlib.pyplot as plt

print('           \033[1m   NON-PARAMETRIC')
print('WILCOXON RANK SUM TEST OF PAIRED SAMPLE\n')
# Extract Data Of Excel Sheet
print('\033[0mWe have 4 Groups E-mail , Website , Both , None')
select_group = input('Select one this is for single/paired: ')
select_group2 = input('Select Second: ')
df = pd.read_excel("data.xlsx")
group1 = df[f'{select_group}']
group2 = df[f'{select_group2}']

# Select Hypotheses
print(f'Ho: M = Difference between {select_group} and {select_group2}')
print(f'H1: M = No difference between {select_group} and {select_group2} \n')

# Wilcoxon Rank Sum Test
wilcoxon_test = mannwhitneyu(group1, group2, alternative='two-sided')
statistic = wilcoxon_test.statistic
pvalue = round(wilcoxon_test.pvalue, 8)
z = stats.norm.ppf(1 - (pvalue / 2))
print('Z-score or normal approximation = ',z)
if pvalue < 0.05:
    print("P-value amounts to", pvalue, " There is sufficient evidence to reject null hypothesis.")
else:
    print("P-value amounts to", pvalue, " There is no sufficient evidence to reject null hypothesis.")

# Plotting
plt.figure(figsize=(8, 4))
x = np.linspace(0, 3, len(group1))
plt.plot(x,np.sort(group1), 'bo-', label=select_group)
plt.plot(x,np.sort(group2), 'ro-', label=select_group2)
plt.axvline(x=1.96, color='r', linestyle='solid', label='Critical region = 1.96')
plt.axvline(x=-1.96, color='r', linestyle='solid', label='Critical region = -1.96')
plt.plot(z, 0.5, 'go', label='P-Value')
plt.xlabel('Cumulative probability')
plt.ylabel('Data Values')
plt.title('Two-Tailed Wilcoxon Sign Paired Sample Test')
plt.legend()
plt.grid(True)
plt.show()
