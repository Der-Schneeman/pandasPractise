"""
author: Philip Schwarzmayr

title: FreeAgent Data Analytics Task

description: Questions on height dataset
            and investigation of the life expectancy dataset
"""

"""
Initialisation
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('mode.chained_assignment', None)

# Opening the height_data.csv file as df
df = pd.read_csv('height_data.csv')

'''What can you conclude about the difference in height for members of group B
    between South America and North America?'''

# Removing Group A
dfB = df.loc[df['group'] == 'B']

dfB1 = dfB[['country','continent','height (cm)']]

# Selecting N.America
N = dfB1.loc[dfB1['continent'] == 'North America']
avgN = N.groupby(['country']).mean()

descN = avgN['height (cm)'].describe()

sortN = avgN.sort_values(by=['height (cm)'])

print('North American Height Data:')
print(descN)

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':5}

sortN.plot()
plt.title("North American Height")
plt.xlabel("Country")
plt.ylabel("Height")


print('\n')

# Selecting S.America
S = dfB1.loc[dfB1['continent'] == 'South America']
avgS = S.groupby(['country']).mean()

descS = avgS['height (cm)'].describe()

sortS = avgS.sort_values(by=['height (cm)'])

print('South American Height Data:')
print(descS)
    
sortS.plot()
plt.title("South American Height")
plt.xlabel("Country")
plt.ylabel("Height")
plt.show()

