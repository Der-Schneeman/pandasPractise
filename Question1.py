"""
author: Philip Schwarzmayr

title: FreeAgent Data Analytics Task

decription: Questions on height dataset
            and investigation on life expectancy dataset
"""

"""
Initialisation
"""
import pandas as pd

# Opening the height_data.csv file as df
df = pd.read_csv('height_data.csv')

'''What fraction of Countries in Europe have an average height above 175cm'''

# Creating data frame of European countries
dfEurope = df[df['continent'] == 'Europe']

# Creating data frame of European countries and height.
dfEurope = dfEurope.sort_values(by="country")
dfC = dfEurope[["country","height (cm)"]]

# Creating data frame of country's average height
avg = dfC.groupby(['country']).mean()

# Get country names of indexes for which height (cm) is <= 175cm
countryNames = avg[ avg['height (cm)'] <= 175 ].index
# Delete these row indexes from Avg
avgB = avg.drop(countryNames , inplace=False)
    
# Print European countries with an average height over 175cm
print('European countries with an average height over 175cm:\n\n', avgB,'\n')

numBig = int(avgB.nunique())
numAll = len(countryNames)

ans = numBig/numAll

print('Fraction of European Countiries with an average height')
print('above 175cm :', ans)

'''Which continent has the highest fraction of countries where 50% or more
   of the members of Group A are above the height of 162cm?'''


    
