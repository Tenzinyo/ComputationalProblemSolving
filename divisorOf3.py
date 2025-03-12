def countDivisor(number):
  count=0
  for i in range(1,number+1):
    if i%3==0:
      count+=1

def divisor(number):
  for i in range(1,number+1):
    if countDivisor(1)==3:
      print(i)
