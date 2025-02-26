totalSum = 0

for num in range(1, 10001):
    sum = 0
    for i in range(1, num):
        if num%i == 0:
            sum += i
    if sum == num:
        totalSum += num

print(totalSum)