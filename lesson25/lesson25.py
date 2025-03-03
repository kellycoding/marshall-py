num = int(input())
greatestPrimeFactor = 1

def primeOrNot(n):
    if n == 2:
        return True
    elif n == 3:
        return True
    else:
        for i in range(3, n, 2):
            if n%i == 0:
                return False
        return True


for i in range(3, num+1, 2):
    if primeOrNot(i) and num%i == 0:
        greatestPrimeFactor = i

if greatestPrimeFactor == 1:
    if num%2 == 0:
        greatestPrimeFactor = 2

print(greatestPrimeFactor)