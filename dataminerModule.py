# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:59:08 2015

@author: Amine Laghaout
"""
# %%

def UpdateNameDB(nameDB, rec, iniYear, finYear):

    ''' 
    Update the counts for a given name 
    
    INPUT: The database nameDB, the new record, and the initial and
    final years.
    
    OUTPUT: The updated database
    '''

    recTuple = (rec[3], rec[1])
    
    # If the name-gender already exists, update the count
    if recTuple in nameDB.keys():
        nameDB[recTuple][rec[2]-iniYear] += rec[4] 
        
    # If the name-gender does not exist, create it and initialize the 
    # count
    else:
        nameDB[recTuple] = [0]*(finYear - iniYear + 1)
        nameDB[recTuple][rec[2]-iniYear] += rec[4]

    return nameDB

# %%

def getFileList(pathName):

    ''' 
    Return the list of files corresponding to the wild card passed as 
    an argument
    
    INPUT: A wildcard pathname
    
    OUTPUT: The list of files matching the wildcard
    '''

    from glob import glob   
    fileList = glob(pathName)

    return fileList

# %%

def vectorizeFile(filePath):
    
    ''' 
    Convert the data file into a list 
    
    INPUT: A file name
    
    OUTPUT: A list which contains the comma-separated data of the file
    '''

    import os.path 
    
    fileExtension = os.path.splitext(filePath)[1][1:].lower()

    imageFileExt = ['txt', 'csv']
    
    # Make sure the file has the right extension
    if fileExtension in imageFileExt:

        from pandas import read_csv
        
        dataVector = read_csv(filePath, header = None)
 
    else:
        # TO-DO: Handle different input files
        print('ERROR')
      
    return dataVector.values.tolist()

# %%

def PopulateDB(nameDB, nameList, iniYear, finYear):
    
    ''' 
    Populate the database from a given input file 
    
    INPUT: The database, the list of entries, the initial and final 
    years
    
    OUTPUT: The database updated with the new entries.
    '''    
    
    for rec in nameList:

        nameDB = UpdateNameDB(nameDB, rec, iniYear, finYear)

    return nameDB
    
def loadData(pathName, iniYear, finYear):

    ''' 
    Populate the database from all the input files: This function 
    simply iterates PopulateDB() over all files.   
    '''

    nameDB = {}
    
    for file in getFileList(pathName):
        nameList = vectorizeFile(file)
        print('Processing', file, '...', end = '')
        nameDB = PopulateDB(nameDB, nameList, iniYear, finYear)
        print(' done.')

    return nameDB
    
def MostPopularName(nameDB, Gender):
    
    ''' Return the most popular name of all times for a given gender '''    
    
    nameCount = [sum(nameDB[elem]) for elem in nameDB if elem[1] == Gender]
    keyList = [elem for elem in nameDB if elem[1] == Gender]
    
    mostPopular = keyList[nameCount.index(max(nameCount))][0]
    mostPopularCount = max(nameCount)    
    
    return mostPopular, mostPopularCount

def MostAmbiguous(nameDB, Year, iniYear):

    '''
    This function returns the most gender-ambiguous name in any given 
    year. Gender-ambiguity is defined from the difference of those 
    names attributed to males minus those attributed to females. The
    smaller the difference the largest the ambiguity.
    
    The figure of merit could however be adapted to also include the
    number of occurrences of the names in question. (This is not
    implemented here.)
    '''

    maleList = [elem[0] for elem in nameDB if elem[1] == 'M' and nameDB[elem][Year-iniYear] != 0]
    femaleList = [elem[0] for elem in nameDB if elem[1] == 'F' and nameDB[elem][Year-iniYear] != 0]
    
    ambiguousList = [elem for elem in maleList if elem in femaleList]
    
    difference = [abs(nameDB[elem, 'M'][Year-iniYear]-nameDB[elem, 'F'][Year-iniYear]) for elem in ambiguousList]
    mostAmbiguous = ambiguousList[difference.index(min(difference))]
    
    return mostAmbiguous
    
def MostRateChange(nameDB, Y1, Y2, iniYear):
    
    ''' 
    Returns the names that have most increased and decreased, 
    respectively from year Y1 to year Y2
    '''
    
    popY1 = sum([nameDB[elem][Y1-iniYear] for elem in nameDB])
    popY2 = sum([nameDB[elem][Y2-iniYear] for elem in nameDB])
    rate = [nameDB[elem][Y2-iniYear]/popY2 - nameDB[elem][Y1-iniYear]/popY1 for elem in nameDB]
    nameList = [elem[0] for elem in nameDB]
    mostIncreased = nameList[rate.index(max(rate))]
    mostDecreased = nameList[rate.index(min(rate))]
    
    return mostIncreased, mostDecreased