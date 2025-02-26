import math

num = int(input())

stoppingNum = -1

for i in range(1, num):
    if stoppingNum == i:
        break
    if num%i == 0:
        print(i)
        if math.floor(num/i) != i:
            print(math.floor(num/i))
        stoppingNum = math.floor(num/i)