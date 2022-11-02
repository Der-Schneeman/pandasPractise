"""
author: Philip Schwarzmayr

title: FreeAgent Data Analytics Task

description: Questions on height dataset
            and investigation of life expectancy dataset
"""

"""
Initialisation
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ast import literal_eval



''' Predicting Life Expectancy for a new country using dataset'''

lifeData = pd.read_csv('life_expectancy_data.csv',header=0,sep=',')

# X is removed since it gives us 35 more clean countries worth of data
X = 'Net Official Development Assist. received (% of GNI)'
lifeData2 = lifeData.drop([X], axis = 1)

colHeadings = lifeData2.columns.values.tolist()  
colHeadings.remove('Country')
colHeadings.remove('Continent')
colHeadings.remove('Region')

cleanData = lifeData2
cleanData = cleanData.replace({'~': ''}, regex=True)

for heading in colHeadings:
    cleanData = cleanData[cleanData[heading] != -99]
    cleanData = cleanData[cleanData[heading] != '-99']
    cleanData = cleanData[cleanData[heading] != '...']
    cleanData = cleanData[cleanData[heading] != '.../...']
    if heading in cleanData:
        cleanData[heading].apply(literal_eval)
        
        # for i in cleanData[heading]:
        #     pd.to_numeric(eval(i))
        #     print(i)

info = cleanData.info()
print(info)

# desc = lifeData2.describe()
# print(desc) 
# desc = cleanData.describe()
# print(desc) 