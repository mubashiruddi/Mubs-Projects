import pandas as pd
import numpy as np
from scipy.stats import kruskal
from scipy.stats import binom
import matplotlib.pyplot as plt
print('\033[1m    NON-PARAMATIC')
print('  Kruskal or H test\n')
#Extract Data Of Ecxel Sheet
print('\033[0mWe have 4 Groups : \033[1mE-mail , Website , Both , None\033[0m')
df=pd.read_excel("data.xlsx")
group1 = df['mail']
group2 = df['Website']
group3 = df['Both']
group4 = df['None']
#Select Hypothese
print('\n\033[1mHo: M = People Equaly trust to take Lab Report from above methods')
print('H1: M = People doesnot Equaly trust to take Lab Report from above methods\n\033[0m')
#Kruskal or H test
H=kruskal(group1,group2,group3,group4)
#Pvalue
pvalue = round(H.pvalue,8)
#Condition
if pvalue > 0.05:
    print(f'\033[1mThe pvalue is {pvalue} There is no significant evidence to reject the null hypotheses\033[0m')
else:
    print(f'\033[1mThe pvalue is {pvalue} There is significant evidence to reject the null hypotheses\033[0m')
y = np.arange(0,len(group1))
x = 2*binom.cdf(y,len(group1),0.5) 
plt.figure(figsize=(8, 4))
plt.plot(x, y, 'bo-')
plt.plot(-1,0)
plt.plot(pvalue,H.statistic, 'ro', label='P-Value')
plt.axvline(x=0.05, color='r', linestyle='solid', label='Critical region (alpha = 0.05)')
plt.ylabel('Number of Observation')
plt.xlabel('Cumulative probability')
plt.title('Two-Tailed Kruskal or H Test')
plt.legend()
plt.show()
