import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import binom
import matplotlib.pyplot as plt

print('           \033[1m   NON-PARAMATIC')
print('WILCOXON SIGN RANK TEST OF PAIRED SAMPLE\n')
#Extract Data Of Ecxel Sheet
print('\033[0mWe have 4 Groups E-mail , Website , Both , None')
select_group = input('Select one this is for single/paired ')
select_group2 = input('Select Secound ')
df=pd.read_excel("data.xlsx")
group1 = df[f'{select_group}']
group2 = df[f'{select_group2}']
difference = (group2-group1)
#Select Hypothese
print(f'Ho: M = NO difference between {select_group} and {select_group2}')
print(f'H1: M = Difference between {select_group} {select_group2} \n')
#Apply Wilcoxon sign rank paired test
Wilcoxon = stats.wilcoxon(group1,group2)
static = Wilcoxon.statistic
pvalue = round(Wilcoxon.pvalue,8)
z = stats.norm.ppf(1 - (pvalue / 2))
#Condition for Critical value
if pvalue < 0.05:
    print("P-value amounts to", str(pvalue), " There is suffiecient evidence to reject null hypotheses,  ")
else:
    print("P-value amounts to", str(pvalue), " There is no suffiecient evidence to reject null hypotheses,  ")
 
x = np.linspace(0, 5.0, len(difference))
plt.figure(figsize=(8, 4))
plt.plot(x,np.sort(group1), 'yo-', label=select_group)
plt.plot(x,np.sort(group2), 'ro-', label=select_group2)
plt.plot(x, np.sort(difference), 'bo-', label="Difference")
plt.plot(z,0, 'go', label='P-Value')
plt.axvline(x=1.96, color='r', linestyle='solid', label='Critical region (alpha = 0.025)')
plt.axvline(x=-1.96, color='r', linestyle='solid', label='Critical region (alpha = 0.025)')
plt.ylabel('Number of Observation')
plt.xlabel('Cumulative probability')
plt.title('Two-Tailed Wilcoxon Sign Paired sample Test')
plt.grid(True)
plt.legend()
plt.show()

print('\n            NON-PARAMATIC')
print('WILCOXON SIGN RANK TEST OF SINGLE SAMPLE')
Wilcoxon = stats.wilcoxon(group1)
pvalue = round(Wilcoxon.pvalue,8)
static = Wilcoxon.statistic
difference = group1 - np.median(group1)
if pvalue < 0.05:
    print("P-value amounts to", str(pvalue), " There is suffiecient evidence to reject null hypotheses,  ")
else:
    print("P-value amounts to", str(pvalue), " There is no suffiecient evidence to reject null hypotheses,  ")
#y = np.arange(0,difference)
#x = 2*binom.cdf(y,difference,0.5) 
x = np.linspace(0, 1.5, len(difference))
plt.figure(figsize=(8, 4))
plt.plot(x,np.sort(group1), 'yo-', label=select_group)
plt.plot(x, np.sort(difference), 'bo-', label="Difference")
plt.plot(pvalue,0, 'go', label='P-Value')
plt.axvline(x=0.05, color='r', linestyle='solid', label='Critical region (alpha = 0.05)')
plt.ylabel('Number of Observation')
plt.xlabel('Cumulative probability')
plt.title('Two-Tailed Wilcoxon Sign single sample Test ')
plt.grid(True)
plt.legend()
plt.show()

