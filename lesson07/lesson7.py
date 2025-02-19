from random import randrange

try:
    dc = int(input())
except:
    print("Please enter an integer")
    quit()

d20 = randrange(1, 21)

if d20 >= dc:
    print("You succeeded the ability check")
else:
    print("You did not succeed the ability check")