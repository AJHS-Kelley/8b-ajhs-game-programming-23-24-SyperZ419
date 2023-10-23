import random
# FUNCTION -- a named piece of code that can be reused easily. 
# FUNCTION SIGNATURE -- Syntax for creating a new function. 
def exampleFunctionA(): # NO PARAMETERS
    count = 0
    num = int(input("How many times do you want to wish a happy birthday?\n"))
    while count < num:
        print("Happy Birthday!")
        count += 1

def exampleFunctionB(num, count): # PARAMETERS
    while count < num:
        print("Happy Birthday!")
        count += 1

# IF A FUNCTION REQUIRES PARAMETERS, YOUR CODE WILL CRASH WITHOUT THEM!

# RUNNING A FUCTION IS KNOWN AS CALLING THE FUNCTION
# exampleFunctionA()
# exampleFunctionB(5, 0)

def rollDice(numDice, sizeDice):
    numRolled = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        print(f"Roll: {roll}\n")
        numRolled += 1

rollDice(4, 12)
rollDice(3, 20)




