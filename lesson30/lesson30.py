num = int(input())

if num%2 == 0:
    output = "10"*int((num/2))
else:
    output = "10"*int(((num+1)/2))
    output = output[:-1]

for i in range(num):
    print(output[:i+1])