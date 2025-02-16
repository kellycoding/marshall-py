# Lesson 4
import math

cans = 0
for i in range(3):
    section = input()
    cans += len(section)

leftover = 0
packs = 0 # packs of 12 cans

packs = math.ceil(cans/12)
leftover = int(packs)*12 - cans

print(cans)
print(leftover)
print(packs*14.95)