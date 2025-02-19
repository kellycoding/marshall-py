for i in range(6):
    games = input()
    wins = games.count("W")
    
    if wins == 0:
        print("The player is eliminated")
    else:
        if wins < 3:
            group = 3
        elif wins < 5:
            group = 2
        else:
            group = 1
        print(f"The player is placed in group {group}")