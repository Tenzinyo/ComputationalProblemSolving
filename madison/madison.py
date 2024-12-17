"""
@author: tenzinuden
"""

def madison():
    readfile=open('madison_temp.csv','r')
    header=readfile.readline()
    dates=[]
    maxi=[]
    mini=[]
    for rawline in readfile:
        row=rawline.split(',')
        dates.append(row[2])
        maxi.append([3])
        mini.append([4])
    readfile.close()
    return dates,maxi,mini
print(madison())

def madisonlist():
    file=open('madison_temp.csv')
    header=file.readline()
    table=[]
    i=0
    for line in file:
        row=line.split(',')
        row[3]=int(row[3])
        row[4]=int(row[4])
        table.append([row[2], row[3],row[4]])
        # table.append(row[2:])
    file.close()
    print(len(table))
    return table
madisonlist()
    

tempTable=madisonlist() 
print(len(tempTable[0][1]))

def printTable():
    table=madisonlist()
    date=[]
    numROW=len(table)
    numC=len(table[0])
    for r in range(numROW):
        print('value of row',r)
        for c in range(numC):
            print(table[r][c])
    return None
print(printTable())


def readDataLists():
    file=open('madison_temp.csv')
    header=file.readline()
    date=[]
    maxTemp=[]
    minTemp=[]
    for line in file:
        row=line.split(',')
        date.append(row[2])
        maxTemp.append(int(row[3]))
        minTemp.append(int(row[4]))
    file.close()
    return date, maxTemp, minTemp

readDataLists()

    
    
def data():
    file=open('2.5_month.csv','r')
    header=file.readline()
    time=[]
    latitude=[]
    longitude=[]
    mag=[]
    for line in file:
        row=line.split(',')
        time.append(row[1])
        latitude.append(row[2])
        longitude.append(row[3])
        mag.append(row[4])
    file.close()
    return time,latitude,longitude,mag
print(data())

def dataList():
    file=open('2.5_month.csv')
    header=file.readline()
    table=[]
    i=0
    for line in file:
        row=line.split(',')
        row[2]=int(row[2])
        row[3]=int(row[3])
        row[4]=int(row[4])
        table.append(row[1],row[2],row[3],row[4])
    file.close()
    print(len(table))
    return table
dataList()

def printTable():
    table=dataList()
    time=[]
    numRow=len(table)
    numC=len(table[0])
    for r in range(numRow):
        print('value of row')
        for c in range(numC):
            print(table[r][c])
    return None
print(printTable())


def readSATData():
    dataFile = open('8.1.csv')
    headder = dataFile.readline() 
    table = []
    i=0;
    for line in dataFile:
        row = line.split(',')
        table.append([row[0], int(row[1]), int(row[2])])
        
    dataFile.close()
    print(table)
    return table
readSATData()

def satList():
    file=open('8.1.csv')
    header=file.readline()
    table=[]
    i=0;
    for line in file:
        row=line.split(',')
        table.append(((row[0]),int(row[1]),int(row[2])))
       
    file.close()
    print('     ID   MATH   ERBW')
    print('   -----  ----  -----')
    for row in table:
        print('{0:>8s} {1:>5} {2:>5} '.format(row[0], row[1],row[2]))

satList()


def getMinTemp(table, date):
    tempTable=satList()
    numRows = len(table)
    for r in range(numRows):
        if table[r][0] == date:
            return(table[r][2])
    return None
getMinTemp(tempTable,'20131101')

import urllib.request as web
def earthquake():
    url='http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv'
    quakeFile=web.urlopen(url)
    header=quakeFile.readline()
    table=[]
    for line in quakeFile:
        line=line.decode('utf-8')
        row=line.split(',')
        latitude=float(row[1])
        longitude=float(row[2])
        depth=float(row[3])
        magnitude=float(row[4])
        table.append([latitude,longitude,depth,magnitude])
    quakeFile.close()
    return table
earthquake()

def printTable(quarkTable):
    print('latitude    longtitude    depth    magnitude')
    print(' -------    ----------    -----    ---------')
    for row in quarkTable:
     
        print('{0:>8.2f} {1:>9.2f} {2:>5.1f} {3:>6.1f}'.format(row[0],row[1],row[2], row[3]))
        
printTable(earthquake())
        
