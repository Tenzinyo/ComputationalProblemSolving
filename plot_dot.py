import matplotlib.pyplot as pyplot 
text1='AVDGEY'
text2='AVhrYG' 
text1=text1.lower()
text2=text2.lower()
x=[]
y=[]
for index1 in range(len(text1)):
    for index2 in range(len(text2)):    #if you want to apply the first value to all, use ested loop
        if text1[index1]==text2[index2]:
              print(x.append(index1))
              print(y.append(index2))
pyplot.scatter(x, y)
pyplot.xlim(0, len(text1))
pyplot.ylim(0, len(text2))
pyplot.xlabel(text1)
pyplot.ylabel(text2)
pyplot.show()

text1='aceg'
text2='bdfh'
for index in range(len(text1)):
    print(text1[index]+text2[index])
    
text1='abcd'
text2='aaz'
for index2 in range(len(text2)):
    for index1 in range(len(text1)):
        if text1[index1]==text2[index2]:
            print(index1,index2)

text='imho'
for index1 in range(len(text)):
    for index2 in range(len(text)):
        print(text[index1:index2+1])
        
    
text1='two'
text2= 'words'
for index1 in range(len(text1)):
    for index2 in range(len(text2)):
        if text1[index1]==text2[index2]:
            print(text[index1],index1,index2)
            
text='apple'
text1='aplle'
for index in range(len(text)):
    if text[index]==text1[index]:
        print(text[index],text1[index])
       