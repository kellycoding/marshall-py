balance = float(input())
cookies = input()

for i in range(len(cookies)):
    if cookies[i] != "b" and cookies[i] != "c":
        print(f"{cookies[i]} is not a valid input")
        quit()

big = cookies.count("b")
normal = cookies.count("c")
revenue = (2.00*big) + (1.25*normal)
cost = (0.75*big) + (0.50*normal)

print(f"We sold {big + normal} cookies. We made {revenue-cost} in profit. Our total balance is {balance + revenue - cost}.")