n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    term1 = 0
    term2 = 1
    newTerm2 = -1
    for i in range(n-1):
        newTerm2 = term1 + term2
        term1 = term2
        term2 = newTerm2
    print(term1)