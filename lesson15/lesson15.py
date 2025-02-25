conditionVariable = True
password = "poop"

while conditionVariable:
    userInput = input("Guess the password: ")
    
    if userInput == password:
        print("Yay!")
        conditionVariable = False
    else:
        print(":(")

userInput = input("Search for a fruit: ")

fruits = ["Apple", "Banana", "Kiwi", "Strawberry"]
found = False

for fruit in fruits:
    if userInput == fruit:
        print("Fruit found!")
        found = True
        break

if found == False:
    print("Fruit not found")