str1, str2 = input(), input()
characters = []

if len(str1) > len(str2):
    longerString = str1
    shorterString = str2
    stringLength = len(str1)
else:
    longerString = str2
    shorterString = str1
    stringLength = len(str2)

for i in range(stringLength):
    if longerString[i] in shorterString and not longerString[i] in characters:
        characters.append(longerString[i])

print(sorted(characters))