import pandas as pd
import numpy as np
import statistics
from scipy.stats import binomtest, binom
import matplotlib.pyplot as plt
print('\033[1m    NON-PARAMATIC')
print('SIGN TEST OF PAIRED SAMPLE\n')
#Extract Data Of Ecxel Sheet
print('\033[0mWe have 4 Groups E-mail , Website , Both , None')
select_group = input('Select one ')
select_group2 = input('Select Secound ')
df=pd.read_excel("data.xlsx")
group1 = df[f'{select_group}']
group2 = df[f'{select_group2}']
#Select Hypothese
print(f'\n\033[1mHo: M > People Trust {select_group} more than {select_group2} for lab report')
print(f'H1: M < People Trust {select_group} less than {select_group2} for lab report')
#Calculate Differences, Positive&Negative Value
difference=group1-group2
difference = [x for x in difference if x<0 or x>0]
pos_value = len([x for x in difference if x>0])
neg_value = len([x for x in difference if x<0])
n = pos_value + neg_value
#Condition of large and small sample
#Calculate Pvalue and Conditions
if n > 10:
    if pos_value > n/2:
        z = min(pos_value,neg_value) - 0.5
    else:
        z = min(pos_value,neg_value) + 0.5
    z = (z-(n/2))/(0.5* pow(n,0.5))
    if -1.645 < z and z < 1.645:
        print("\n\033[1mP-value amounts to", str(z), " There is no suffiecient evidence to reject null hypotheses,  ")
    else:  
        print("\n\033[1mP-value amounts to", str(z), " There is suffiecient evidence to reject null hypotheses,  ")
    y = np.arange(0,n)
    x = binom.cdf(y,n,0.5) 
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, 'bo-')
    plt.plot(z,0,'ro', label='P-Value')
    plt.axvline(x=1.645, color='r', linestyle='solid', label='Critical region (alpha = 0.025)')
    plt.axvline(x=-1.645, color='r', linestyle='solid', label='Critical region (alpha = 0.025)')
    plt.axhline(y=pos_value, color='orange', linestyle='--', label=f'Observed statistic (k = {pos_value})')
    plt.ylabel('Number of Observation')
    plt.xlabel('Cumulative probability')
    plt.title('One-Tailed Sign Test - Cumulative Distribution Function')
    plt.legend()
    plt.show()                
else:
    if pos_value > neg_value:
        prefrence_value = pos_value
        pvalue = binomtest(pos_value,n,p=0.5,alternative='less')
    elif pos_value < neg_value:
        prefrence_value = neg_value
        pvalue = binomtest(neg_value,n,p=0.5,alternative='greater')
    pvalue = pvalue.pvalue
    pvalue = round(pvalue,8)
    #print Value
    print('\n\033[0mPositive value = ', pos_value)
    print('Negative value = ', neg_value)
    print('Observation value = ', n)
    #Hypothesis Condition
    if pvalue < 0.05:
        print("\n\033[1mP-value amounts to", str(pvalue), " There is suffiecient evidence to reject null hypotheses,  ")
    else:  
        print("\n\033[1mP-value amounts to", str(pvalue), " There is no suffiecient evidence to reject null hypotheses,  ")
    y = np.arange(0,n)
    x = 2*binom.cdf(y,n,0.5) 
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, 'bo-')
    plt.plot(pvalue,0,'ro', label='P-Value')
    plt.axvline(x=0.05, color='r', linestyle='solid', label='Critical region (alpha = 0.05)')
    plt.axhline(y=prefrence_value, color='orange', linestyle='--', label=f'Observed statistic (k = {prefrence_value})')
    plt.ylabel('Number of Observation')
    plt.xlabel('Cumulative probability')
    plt.title('One-Tailed Sign Test - Cumulative Distribution Function')
    plt.legend()
    plt.show()            