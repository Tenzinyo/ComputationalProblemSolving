##################
### UNIT TESTS ###
##################
def test_numberOfDigits():
    assert numberOfDigits(1) == 1
    assert numberOfDigits(9) == 1
    assert numberOfDigits(10) == 2
    assert numberOfDigits(99) == 2
    assert numberOfDigits(100) == 3
    assert numberOfDigits(12345) == 5
    assert numberOfDigits(0) == 1
    print("numberOfDigits() passes all tests")
    
def test_allSameDigit():
    # TODO: write these tests and delete the next line
    assert allSameDigit(23)== False 
    assert allSameDigit(0)== True
    assert allSameDigit(11)== True 
    assert allSameDigit(333)==True 
    
    print("allSameDigit() passes all tests")
allSameDigit(2)
def test_isDivisor():
    assert isDivisor(2, 4) == True
    assert isDivisor(4, 1) == False
    assert isDivisor(3, 25) == False
    assert isDivisor(1, 37) == True
    assert isDivisor(2, 0)== True
    assert isDivisor(0, 2)==False
    assert isDivisor(float, float)==False
    passed = 'some'
    passed = test_isDivisor_preconditions()
    print("isDivisor() passes "+passed+" tests")
def test_isDivisor_preconditions():
    # The tests below check that preconditions are enforced.
    # Note that we will almost NEVER catch AssertionError like this.
    try:
        r = isDivisor(0, 4)
        raise RuntimeError("expected AssertionError on previous line")
    except AssertionError as ae:
        pass
    try:
        r = isDivisor(2.0, 4)
        raise RuntimeError("expected AssertionError on previous line")
    except AssertionError as ae:
        pass
    try:
        r = isDivisor(2, 4.0)
        raise RuntimeError("expected AssertionError on previous line")
    except AssertionError as ae:
        pass
    print("isDivisor() passes precondition tests")
    return 'all'
def test_isPrime():
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(6) == False
    assert isPrime(49) == False
    assert isPrime(61) == True
    assert isPrime(367) == True
    assert isPrime(391) == False
    assert isPrime(1) == False
    assert isPrime(0) == False
    assert isPrime(-7) == False
    print("isPrime() passes all tests")
def test_nextPrime():
    assert nextPrime(2) == 3
    assert nextPrime(3) == 5
    assert nextPrime(6) == 7
    assert nextPrime(7) == 11
    assert nextPrime(10) == 11
    assert nextPrime(49) == 53
    assert nextPrime(61) == 67
    assert nextPrime(1) == 2
    assert nextPrime(0) == 2
    assert nextPrime(-7) == 2
    print("nextPrime() passes all tests")
def test_isPerfect():
    assert isPerfect(1) == False
    assert isPerfect(10) == False
    assert isPerfect(100) == False
    assert isPerfect(6) == True
    assert isPerfect(28) == True
    assert isPerfect(496) == True
    assert isPerfect(8128) == True
    print("isPerfect() passes all tests")
def test_leapYear():
    # TODO: write these tests and delete the next line
    assert leapYear(0)==True
    assert leapYear(11111)==False
    assert leapYear(3000)==False
    assert leapYear(2000)==True
    assert leapYear(2020)==True
    assert leapYear(1752)==True
    assert leapYear(1758)==False
    print("leapYear() passes all tests")
    
def test_nextLeapYear():
    # TODO: write these tests and delete the next line
    assert nextLeapYear(1111)==1112

def test():
    test_numberOfDigits()
    test_allSameDigit()
    test_isDivisor()
    test_isPrime()
    test_nextPrime()
    test_isPerfect()
    test_leapYear()
    test_nextLeapYear()
test()