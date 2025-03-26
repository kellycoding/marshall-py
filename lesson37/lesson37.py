word = input()
compressed = ""
currentChar = ""
charCount = 1

for i in range(len(word)):
    if not currentChar:
        currentChar = word[i]
    elif word[i] == currentChar:
        charCount += 1
    else:
        compressed += currentChar
        compressed += str(charCount)
        currentChar = word[i]
        charCount = 1

compressed += currentChar
compressed += str(charCount)
if len(compressed) < len(word):
    print(compressed)
else:
    print(word)