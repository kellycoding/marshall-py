for i in range(50):
    if (i+1)%15 == 0:
        print("FizzBuzz")
    elif (i+1)%5 == 0:
        print("Buzz")
    elif (i+1)%3 == 0:
        print("Fizz")
    else:
        print(i+1)