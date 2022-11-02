"""
author: Philip Schwarzmayr

title: FreeAgent Data Analytics Task

description: Questions on height dataset
            and investigation on life expectancy dataset
"""

"""
Initialisation
"""
import numpy as np
import pandas as pd

pd.set_option('mode.chained_assignment', None)

# Opening the height_data.csv file as df
df = pd.read_csv('height_data.csv')

'''Which continent has the highest fraction of countries where 50% or more
   of the members of Group A are above the height of 162cm?'''

# Removing Group B

# Get id names of indexes for which group is A
dfA=df.loc[df['group'] == 'A']

# Removing Group and ID column
dfA1 = dfA[["country", "continent", "height (cm)"]]

# Creating array of continent names
continentNames = (dfA1['continent'].unique())

overFifty = pd.DataFrame(columns = ['continent','total','numOver','fraction'],\
                                 index = [1, 2, 3, 4, 5, 6])
overFifty['continent'] = continentNames

zeros = np.zeros(6)
overFifty['numOver'] = zeros

count = 1
for region in continentNames:
    
    dfreg = dfA1.loc[dfA1['continent'] == region]
    
    # Creating array of country names in this continent
    countryNames = (dfreg['country'].unique())
    
    regionTotal = len(countryNames)
    overFifty['total'].loc[count] = regionTotal
    
    
    for name in countryNames:
        
        dfTotal = dfreg.loc[(dfreg['country'] == name)]
        
        total = len(dfTotal)
        
    
        dfOver = dfreg.loc[(dfreg['country'] == name)\
                          & (dfreg['height (cm)'] > 162 )]
            
        over = len(dfOver)  
        
        percent = (over/total)*100
        
        if percent >= 50:
            overFifty['numOver'].loc[count] += 1
    
    overFifty['fraction'].loc[count] = overFifty['numOver'].loc[count]\
                                        / regionTotal
    
    count += 1
    
largestFraction = overFifty[overFifty.fraction == overFifty.fraction.max()]
lfContinent = largestFraction.iloc[0:1, 0:1]

print(lfContinent,'has the largest fraction!')
        

 
        
        

 
    

    
