import dice


roll1 = dice.display(1, 6)
roll2 = dice.display(1, 6)

if dice.isDoubles(roll1, roll2):
    print("You rolled a double. Go again.")
else:
    print("It was not a double.")