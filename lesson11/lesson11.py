point = list(map(int, input("Please enter two coordinates: ").split()))

if len(point) != 2:
    print("Pleasse enter only two coordinate values")
elif not point[0] or not point[1]:
    print("The coordinate is not in a quadrant")
elif point[0] > 0:
    if point[1] > 0:
        print("Quadrant 1")
    else:
        print("Quadrant 4")
else:
    if point[1] > 0:
        print("Quadrant 2")
    else:
        print("Quadrant 3")