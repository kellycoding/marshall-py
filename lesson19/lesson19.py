num = input()

try:
    int(num)
except:
    print("Not an integer")
    quit()

num = int(num)
prime = True

if num == 1:
    prime = False
elif num == 2:
    pass
elif num % 2 == 0:
    prime = False
else:
    for i in range(3, num+1, 2):
        if i != num and num%i == 0:
            prime = False
            break

if prime == True:
    print("Prime")
else:
    print("Not prime")