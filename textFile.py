"""
Created on Fri Oct 21 08:13:58 2022
@author: tenzinuden
"""

import textlib
text=textlib.normalize("Walla Walla")
print(text)
new=textlib.splitIntoWords("I am just a little human trying to save the world!")
print(new)
newT=textlib.removePunctuation(new)
print(newT)
def readFile(fileName):
    #text.txt="Whihtgbh  nhnyjny"
    textFile=open(fileName,'r')
    text=textFile.read()
    print(text)
    textFile.close()
readFile("conundra.py")


def readFile(fileName):
     #text.txt="Whihtgbh  nhnyjny"
     textFile=open(fileName,'w')
     text=textFile.write()
     print(text)
     textFile.close()
readFile("tx.py")

#to copy file
import textlib
def wordCountFile(fileName):
    textFile=open(fileName,'r',encoding='utf-8')
    text=textFile.read()
    newTextFile=open("copyOf_NEXTPRIME.py",'w')
    print(text)
    newTextFile.write(text)
    textFile.close()
wordCountFile("nextprime.py")

def lineNumbersFile(FileName):
    textFile=open(FileName,'r', encoding='utf-8')
    newTextFile=open(textFile,'w')
    count=1
    for line in textFile:
        newTextFile('{0:<5}{1}'.format(count, line.rstrip()))
        count=count+1
    textFile.close()
    newTextFile.close()
#lineNumbersFile("textFile","newTextFile")

import urllib.request as web
webPage= web.urlopen('https://www.w3schools.com/python/python_booleans.asp')
rawBytes=webPage.read()
print(rawBytes)
webPage.close()
    
import urllib.request as web
webPage= web.urlopen('https://www.w3schools.com/python/python_booleans.asp')
rawBytes=webPage.read()
text=rawBytes.decode('utf-8') #get in HTML
print(text)
webPage.close()

f=open("pyplot.py","r") 
t=f.read()
f.close() 
print(t)

with open("pyplot.py","r") as f:
    
    t=f.read()
    print(t)

import urllib.request
resp= urllib.request.urlopen("https://web.aiu.ac.jp/")
print(resp.read())

text1='tbontb'
text2='obroob'
count=0
for index in range(len(text1)):
    if text1[index]==text2[index]:
        count+=1
        print(count)


text1='abcd'
text2='dyb'
for  index2 in range(len(text2)):
    for index1 in range(len(text1)):
        if text1[index1]==text2[index2]:
            print(index1,index2)
    
text1='abcd'
text2='bxd'
for  index1 in range(len(text1)):
    for index2 in range(len(text2)):
        if text1[index1]==text2[index2]:
            print(index1,index2)
    
text="imho"
for index1 in range(len(text)):
    for index2 in range(index1,len(text)):
        print(text[index1:index2+1])
    
def find(text,target):
    index=0
    while index<(len(text)):
        if text[index:index+len(target)]==target:
            #finding similar words!!
            newT=text.replace(target,'new')
            return newT
        else:
            index+=1
    return index

def find(text,target):
    index=0
    while index<(len(text)):
        if text[index:index+len(target)]==target:
            return index
        else:
            index+=1
    return index
           
    
sales=[32,42,11,15,58,43,16]
total=0
for item in sales:
   total=total+item
average=total/len(sales)
print(total,average)  

    
sales=[32,42,11,15,58,43,16]
sales=[]
if len(sales)!=0:
    total=0
    for item in sales:
        total=total+item
    average=total/len(sales)
    print(total,average)  


def mean(sales):
    sales=[12,4]
    if len(sales)!=0:
        total=0
    for item in sales:
        total=total+item
    average=total/len(sales)
    return average
print(average)
mean('sales')
    

def min(data):
    min=data[0]
    if len(data)!=0:
        index=0
        for item in data:
            if min>data[index]:
                min=data[index]
            print(min)
min([2,4,3])
                
def sumOdds(data):
    sum=0
    for sum in data:
        if item %2==1:
            sum+=item
    return sum

def countOdds(data):
    count=0
    for item in data:
        if item%2==1:
            count+=1
    return count



    
    
    
    
    
    
