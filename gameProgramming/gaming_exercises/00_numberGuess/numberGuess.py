# Select the secret number from a given range.
# Player must guess a number.
# Compare guess to the secret number.
# What happens if the guess is wrong?
    # Tell them the guess is wrong.
    # Tell them the number of guesses left.
    # Tell them if too high/ too low.
# What happens if the guess is right?
    # Tell them the guess is right.
    # Award a point.
# What happens if the player runs out of guesses?
    # Tell player round has been lost.
    # Award point to CPU.
# Check to see if player or CPU has >= 3 points, if so they win.

import random # Import the random module to our code.

# DECLARATIONS
secretNumber = -1
playerGuess = -1
playerScore = 0
cpuScore = 0
numGuesses = 0
playerName = ""
difficulty = -1
rangeMin = -1
rangeMax = -1
numAttempts = -1

print("""
      *~~~~~~~~~~~~~~~~~~~~~~~~~~*
      |                          |
      |     Guess the Number     |
      |                          |
      |      Xavier Oliver       |
      |          2023            |
      |                          |
      *~~~~~~~~~~~~~~~~~~~~~~~~~~*
        """)

# CPU Secret Number Generation
#secretNumber = random.randint(0, 25)
#print(secretNumber)

# GAME LOOP

# Player Name
playerName = input("Please input the name you would like to be referred to as, then press ENTER\n")
#print("Guess a number from 0 to 25. \nYou have 4 guesses. \nIf you guess it right, you get a point. \nIf you don't get it in four guesses, the CPU gets a point.")
# ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH MATCH
# print() an explanation of your 3 difficulty levels
print(f"Alright {playerName}, please select a difficulty. \nVery Easy (1): The secret number is from 1 - 10, and you get 5 guesses. \nEasy (2): The secret number is from 1 - 20, and you get 5 guesses. \nMedium (3): The secret number is from 1 - 35, and you get 4 guesses.")
print("Hard (4): The secret number is from 1 - 50, and you get 3 guesses. \nVery Hard (5): The secret number is from 1 - 100, and you get 3 guesses.")
# use input() to store difficulty in difficulty variable
# DIFFICULTY SELECT
difficulty = int(input("Type your preferred difficulty number, then press enter.\n"))
# Assign values to numAttempts, rangeMin, and rangeMax based on choice
if difficulty == 1:
    rangeMin = 1
    rangeMax = 10
    numAttempts = 5
elif difficulty == 2:
    rangeMin = 1
    rangeMax = 20
    numAttempts = 5
elif difficulty == 3:
    rangeMin = 1
    rangeMax = 35
    numAttempts = 4
elif difficulty == 4:
    rangeMin = 1
    rangeMax = 50
    numAttempts = 3
elif difficulty == 5:
    rangeMin = 1
    rangeMax = 100
    numAttempts = 3
else:
    # Make this a default setting, print that difficulty wasn't selected properly, use values for normal.  
    print("Selected difficulty option not found. \nDifficulty will default to option 3, Medium.")
    rangeMin = 1
    rangeMax = 35
    numAttempts = 4

print(f"Guess a number from {rangeMin} to {rangeMax}. \nYou have {numAttempts} guesses. \nIf you guess it right, you get a point. \nIf you don't get it in {numAttempts} guesses, the CPU gets a point.")
while playerScore != 3 and cpuScore != 3: # START THE MATCH (GAME)
   # pass -- Tells Python to skip this block of code.

    print(f"{playerName} Score: {playerScore}\nCPU Score: {cpuScore}.\n")
    secretNumber = random.randint(rangeMin, rangeMax)
    # whenever you assign a specific value to something, it's called "hard coded"
    #print(secretNumber)
    # ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH ROUND
    numGuesses = 0
    for guesses in range(numAttempts): # STARTS THE ROUND
        print(f"You have {numAttempts - numGuesses} guesses remaining.\n")
        playerGuess = int(input(f"Type a number from {rangeMin} to {rangeMax}, then press ENTER.\n"))
        # input() saves all data as a STRING by default
        # int() will convert to an INTEGER
        # float() will convert to a FLOAT
        print(f"You have chosen {playerGuess}. Are you correct?\n")
        if playerGuess == secretNumber:
            print("Your guess was correct.\n")
            playerScore += 1
            break # IMMEDIATLY EXIT ANY LOOP YOU ARE IN
        else:
            print("Your guess was incorrect.\n")
            if playerGuess > secretNumber:
                print("Your guess is too high.\n")
            else:
                print("Your guess is too low.\n")
        numGuesses += 1
    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU wins a point since you ran out of guesses.\n")

if playerScore >= 3:
    print(f"{playerName} Wins.\n")
else:
    print("CPU Wins.\n")