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
def fletcherChecksum(text):
    text="Apple"
    checksum1=0
    checksum2=0
    for character in text:
        checksum1=(checksum1+ord(character))%256
    return chr(checksum2)+chr(checksum1)
print(fletcherChecksum("text"))
def verifyMessage(message):
    data=message[:-2]
    checksum=message[-2:]
    if data==checksum:
        return data
    else:
        return ''

