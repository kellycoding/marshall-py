a1, a2, a3 = int(input("Enter angle 1: ")),int(input("Enter angle 2: ")),int(input("Enter angle 3: "))

if a1+a2+a3 != 180:
    print("You did not input a proper triangle")
elif a1 == a2 == a3:
    print("Equilateral")
elif a1 != a2 != a3 and a3 != a1:
    print("Scalene")
else:
    print("Isosceles")