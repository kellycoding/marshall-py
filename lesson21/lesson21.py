num = int(input())

for i in range(1, num+1):
    if i == 1:
        maxFactors = 1
        output = 1
    else:
        factors = 0
        for factor in range(1, i+1):
            if i%factor == 0:
                factors += 1
        if factors > maxFactors:
            maxFactors = factors
            output = i
print(output)