def getEncodedChar(unicode):
    return unicode if unicode <= 122 else getTheRoundedCharacter(unicode)


def getTheRoundedCharacter(unicode):
    return 96 + unicode % 122


def lengthEncoder(string, key):
    encodedString = ""
    key = key % 26
    for i in range(0, len(string)):
        unicode = ord(string[i]) + key
        encodedString += chr(getEncodedChar(unicode))
    return encodedString
