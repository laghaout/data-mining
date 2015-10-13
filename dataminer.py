# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:56:05 2015

@author: Amine Laghaout

Template for a data mining script
"""

import dataminerModule as dmModule

# Path name to the data files with respect to this script.
pathName = './stateData/*.txt' 

# Initial and final year for which we have data. This should utlimately
# be determined on the fly and not hard-encoded.
iniYear = 1910
finYear = 2014 

# Load the data into a dictionary containig the name and gender as its 
# key and the vector of counts from the first to last year as its 
# elements.
nameDB = dmModule.loadData(pathName, iniYear, finYear)

# %% Most popular name

print('***')
MostPopularMale, MostPopularMaleCount = dmModule.MostPopularName(nameDB, 'M')
print('The most popular male name is', MostPopularMale, 'with', 
      MostPopularMaleCount, 'occurrences')

MostPopularFemale, MostPopularFemaleCount = dmModule.MostPopularName(nameDB, 'F')
print('The most popular female name is', MostPopularFemale, 'with', 
      MostPopularFemaleCount, 'occurrences')

# %% Most gender ambiguous name at any given year

print('***')
Year = 1945
mostAmbiguousName = dmModule.MostAmbiguous(nameDB, Year, iniYear)
print('The most gender-ambiguous name in', Year, 'is', 
      mostAmbiguousName)
      
# ERROR: FIGURE OUT WHY THIS IS NOT ALWAYS RETURNING THE SAME RESULT
Year = 2013
mostAmbiguousName = dmModule.MostAmbiguous(nameDB, Year, iniYear)
print('The most gender-ambiguous name in', Year, 'is', 
      mostAmbiguousName) 

# %% Higher increase and highest decreased names

print('***')
Y1 = 1980
Y2 = 2014
mostIncreased, mostDecreased = dmModule.MostRateChange(nameDB, Y1, Y2, iniYear)
print(mostIncreased, 'and', mostDecreased, 'are the names that have undergone the highest percentage increase and decrease, respectively.')