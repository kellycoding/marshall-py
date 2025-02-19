from random import choice

playerChoice = ""

while not playerChoice in {"R", "P", "S"}:
    playerChoice = input("Enter R for rock, P for paper, or S for scissors")

computerChoice = choice(["R", "P", "S"])
if playerChoice == computerChoice:
    print("Tie")
elif playerChoice == "R":
    if computerChoice == "P":
        print("AI wins")
    else:
        print("Player wins")
elif playerChoice == "P":
    if computerChoice == "R":
        print("Player wins")
    else:
        print("AI wins")
else:
    if computerChoice == "R":
        print("AI wins")
    else:
        print("Player wins")