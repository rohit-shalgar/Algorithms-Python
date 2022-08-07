def runLengthEncoding(string):
    charCount = 1
    encodedCharacters = []
    iterableLength = len(string) - 1
    for i in range(0, iterableLength):
        firstChar = string[i]
        secondChar = string[i + 1]
        if secondChar != firstChar or charCount == 9:
            encodedCharacters.append(str(charCount))
            encodedCharacters.append(firstChar)
            charCount = 0
        charCount += 1

    encodeLastCharacter(charCount, encodedCharacters, iterableLength, string)
    return "".join(encodedCharacters)


def encodeLastCharacter(charCount, encodedCharacters, iterableLength, string):
    encodedCharacters.append(str(charCount))
    encodedCharacters.append(string[iterableLength])
