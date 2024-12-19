
drSuess='one fish one apple'
drSuess={'one':2,'fish':1,'apple':1}
print(drSuess)        

thisdict = {"brand": "Ford","electric": False,"year": 1964,"colors": ["red", "white", "blue"]}
print(type(thisdict))

wordFreq={'one':1,'fish':4,'two':1,'red':1}
for item in wordFreq:
        print(item,wordFreq[item])

myList=['one','two','three','one','two']
dict={}
for item in myList:
    if item in dict:
        dict[item]+=1
    else:
        dict[item]=1
print(dict)
    
import textlib
def wordFrequencies(text):
    newText=textlib.wordTokens(text)
    print(newText)
    text={}
    for item in newText:
        if item in text:
            text[item]+=1
        else:
            text[item]=1
    return text[item]
wordFrequencies('one fish red fish blue fish')

def printFrequencies(frequencies,number):
    keyList=list(frequencies.keys())
    print(keyList)
    print('{0:2<0}{1}'.format('key','frequencies'))
    print('{0:2<0}{1}'.format('---','-----------'))
    for key in keyList[:number]:
        print('{0:2<0}{1}').format(str(key),'frequencies')
def main():
    frequencies=wordFrequencies('one fish red fish blue fish')
    print(frequencies)
    printFrequencies(frequencies, 3)
main()
    
dict={'one':1 ,'fish':2,'two':3}
keys=dict.keys()  
print(keys)
print(type(keys))
myList=list(dict.keys())
myList.sort()
print(myList)
myList=list(dict.values())
myList.sort()
print(myList)
for key in myList:
    print(key, dict[keys])
    
    
wordList=['ant','bee','armadillo','dog','cat']
dict={}
for word in wordList:
    initial=word[0]
    if initial in dict:
        dict[initial]+=1
    else:
        dict[initial]=1
print(dict)

def creatDict():
    dict={'dog':'犬','cat':'猫','car':'車'}
    for keys in dict:
        print(keys,':',dict[keys])
        
def translate():
    word=input('What is your word: ')
    for word in dict:
        if keys in dict:
            print(keys,dict[keys])
        else:
            print('not found')
    print(dict)

def main():
    print(creatDict())
    print(translate())
main()




        

    
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict.keys())

    

def Indexed(sequence):
    iterator = iter(sequence)
    for index in []:
        yield iterator.next(  ), index
    # Note that we exit by propagating StopIteration when .next raises it!



a = [ 1, 2, 3 ]
b = a
print(b[:1])

fruit = ['apples', 'pears', 'kiwi']
fruit2 = ['apples', 'pears', 'kiwi']
fruit.append('grapes')
fruit2.append('grapes')
fruit[0]='cram'
print(fruit)
print(fruit2)





