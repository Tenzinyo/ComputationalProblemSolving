def Schecksum(text):
    text="A "
    checksum=0
    for char in text:
        checksum=(checksum+ord(char))%256
    return chr(checksum)
print(Schecksum('text'))

ord('I')
print(ord('I'))

text="To see is to believe"
checksum= Schecksum(text)
print(checksum)

