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
