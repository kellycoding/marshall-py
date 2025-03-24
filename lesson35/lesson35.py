items = [1, 1, 0, 0, 9, 8, 76, 4, 43, 57, 8]

newitems = []
for i in items:
    if not i in newitems:
        newitems.append(i)

print(newitems)