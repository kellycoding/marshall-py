number = input() + input() + input() + input()

if number[0] in {"8", "9"} and number[1] == number[2] and number[3] in {"8", "9"}:
    print("Telemarketer")
else:
    print("Not telemarketer")