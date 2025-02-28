longestLength = 0
longestName = ""

while True:
    name = input()
    if name == "X":
        break
    
    if len(name) > longestLength:
        longestLength = len(name)
        longestName = name

print(longestName)