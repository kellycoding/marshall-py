sum = 0
loops = 0

while True:
    num = input()
    try:
        num = int(num)
    except:
        print(sum/loops)
        break
    
    sum += int(num)
    loops += 1