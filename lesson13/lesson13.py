m, d = int(input("Enter a numerical month: ")), int(input("Enter a numerical day:"))

if not 0<m<=12 or not 0<d<=31:
    print("Please enter a valid date")
elif m in {4,6,9,11} and not 0<d<=30:
    print("Please enter a valid date")
elif m == 2 and not 0<d<=28:
    print("Please enter a valid date")
else:
    if m<2 or (m==2 and d<18):
        print("Before")
    elif m==2 and d==18:
        print("Special")
    else:
        print("After")