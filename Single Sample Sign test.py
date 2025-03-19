import pandas as pd
import numpy as np
from scipy.stats import binomtest ,binom,norm
import matplotlib.pyplot as plt
print('\033[1m      NON-PARAMATIC')
print('SIGN TEST OF SINGLE SAMPLE')
#Extract Data Of Ecxel Sheet
print('\n\033[0mWe have 4 Groups E-mail , Website , Both , None')
select_group = input('Select any one ')
df=pd.read_excel("data.xlsx")
group1 = (df[f'{select_group}'])
Median_value = int(np.median(group1))
#Select Hypothese
print(f'\n\033[1mHo: M = People Trust {select_group} for lab report')
print(f'H1: M = People doesnot Trust {select_group} for lab report\n')
#Calculate Differences and Positive,Negative Values
difference = [x - Median_value for x in group1]
difference = [x for x in difference if x<0 or x>0]
pos_value=len([x for x in difference if x>0])
neg_value=len([x for x in difference if x<0])
n = pos_value + neg_value
#Calculate Pvalue & Z value and Conditions
print('\033[0mPositive Value = ',pos_value)
print('Negative Value = ',neg_value)
print('Observation Value = ',n)
if n > 25:
    if pos_value > n/2:
        z = min(pos_value,neg_value) - 0.5
    else:
        z = min(pos_value,neg_value) + 0.5
    z = (z-(n/2))/(0.5* pow(n,0.5))        
    pvalue = 2*(norm.cdf(z))
    k = 0.05
    if pvalue > k:
        print("\n\033[1mP-value amounts to", str(pvalue), " There is no suffiecient evidence to reject null hypothesis,  ")
    else:
        print("\n\033[1mP-value amounts to", str(pvalue), "There is sufficient evidence to reject null hypothesis ")
else:
    k=0
    while binom.cdf(k,n,0.5) < 0.05:
        k+=1
    
    if min(pos_value,neg_value) > k:
        print("\n\033[1mP-value amounts to", str(min(pos_value,neg_value)), " There is no suffiecient evidence to reject null hypothesis,  ")
    else:
        print("\n\033[1mP-value amounts to", str(min(pos_value,neg_value)), "There is sufficient evidence to reject null hypothesis ")

y = np.arange(0,n)
x = 2*binom.cdf(y,n,0.5) 
plt.figure(figsize=(8, 4))
plt.plot(x, y, 'bo-')
plt.plot(-1,0)
plt.plot(0,min(pos_value,neg_value), 'ro', label='P-Value')
plt.axvline(x=k, color='r', linestyle='solid', label='Critical region (alpha = 0.05)')
plt.axhline(y=min(pos_value, neg_value), color='orange', linestyle='--', label=f'Observed statistic (k = {min(pos_value, neg_value)})')
plt.ylabel('Number of Observation')
plt.xlabel('Cumulative probability')
plt.title('Two-Tailed Sign Test')
plt.legend()
plt.show()        