import array as myarray
arr = myarray.array('i',[1,5,3])
arr1 = myarray.array('d',[2,4,5,6,3])
arr2 = myarray.array('u', ['a','j'])
print(arr.typecode)
print(len(arr))
slice = arr[:-1]
print("slice is ", slice)

for i in range(0,len(arr)):
    print("value is " , arr[i])

x = list(range(0,10000,3))
search = myarray.array('i',x)
for i in range(0,len(arr)):
    print("search is " , search[i])
