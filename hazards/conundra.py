def numberOfDigits(number):
    
    """Return the number of digits in number (in decimal).
    
    Parameters:
        number: a nonnegative integer
    
    Return value:
        the number of digits required to represent the number
    """
    # TODO: write this
    assert isinstance (number,int), 'number must be a nonnegative integer'
    assert number>=0,"number must be >= 0"
    numberOfDigits=0
    if number == 0:
        return 1
    while number!=0:
        number=number//10
        numberOfDigits +=1
    # TODO: write this
    return numberOfDigits

    
def allSameDigit(number):
    """Return whether all digits in (decimal) number are the same.
    
    Parameters:
        number: a nonnegative integer
        
    Return value:
        whether all digits in number (as a decimal) are the same
    """
    assert isinstance(number, int), "number must be an integer"
    assert number >= 0, "number must be >= 0"
    residue = number
    lastDigit = number % 10
    while residue != 0:
        digit = residue % 10
        if digit != lastDigit:
            return False
        residue = residue // 10
    return True

def isDivisor(divisor, number):
      """Return whether divisor evenly divides number.
      
      Parameters:
          divisor: a non-zero integer
          number:  an integer
          
      Return value:
          whether divisor evenly divides number
      """
      
      if divisor==0:
          return False
      if divisor==float:
          return False
      if number==float:
          return False
      
      assert isinstance(number,int)
      assert isinstance(divisor,int) 
      assert divisor>0
      remainder=number%divisor
      if remainder==0:
          return True
      else:
          return False


def isPrime(number):
    """Return whether number is prime.
    
    Parameters:
        number: an integer
    
    Return value:
        whether number is a prime number
    
    Note: a prime number is a positive integer greater than 1 that
    has no divisors except 1 and itself.
    From Ex 5.4.24.
    """
    # TODO: write this, making use of isDivisor()
    if number<2:
        return False
    if number==2:
        return True
    for num in range(2,number):
        if isDivisor(num, number):
            return False
    return True

def nextPrime(number):
    """Return the next prime number larger than number.
   
    Parameters:
        number: an integer
    
    Return value:
        the next prime number larger than number
    
    From Ex 5.4.25.
    """
    # TODO: write this, making use of isPrime()
    newn=number + 1
    if isPrime(number):
        number=number+1
        
    while not isPrime(newn):
        newn= newn + 1
    return newn 
def isPerfect(number):
    """Return whether number is perfect.
    
    Parameters:
        number: a positive integer
        
    Return value:
        True if number is perfect.
    
    A perfect number is a positive integer for which the sum of all of
    its positive divisors (less than itself) is equal to the number.
    """
    # OPTIONAL: do for a possible mark of Exemplary
    # TODO: write this, making use of isDivisor()
    assert isinstance(number,int)
    assert number>=0
    sumAll=0
    
    for num in range(1, number):
        if isDivisor(num, number):
            sumAll=sumAll+num
           
    if sumAll==number:
        return True
    else:
        return False
              
def leapYear(year):
    """Return whether year is a leap year (under British law).
    
    Parameters:
        year: a positive integer year
        
    Return value:
        True if the year is a leap year.
    
    Note: years 1 through 1752 are under Julian calendar, for which
    every year divisible by 4 is a leap year. Years after 1752 are 
    under the Gregorian calendar, in which years divisible by 100
    are _not_ leap years unless they are divisible by 400.
    
    While inspired by Ex 5.4.4, this accurately reflects the
    change in calendars--and the fact that there is no year 0.
    """
    assert isinstance(year, int), "year must be an integer"
    #assert year >= 1, "year must be positive"
    return year % 4 == 0 and not (year > 1752
                                  and year % 100 == 0
                                  and year % 400 != 0)

    
def nextLeapYear(afterYear):
    """Return the next leap year following afterYear.
    
    Parameter:
        afterYear: a year CE (integer >= 1)
    
    Return value:
        the next leap year after afterYear
    """
    assert isinstance(afterYear, int) and afterYear >= 1, \
        "year must be an integer and at least 1"
    if afterYear==0:
        return 4
    year = afterYear + 1
    while True:
        if leapYear(year):
            return year
        year = year + 1