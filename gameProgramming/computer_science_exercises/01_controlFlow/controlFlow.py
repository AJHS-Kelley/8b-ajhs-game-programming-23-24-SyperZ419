#  Control Flow, Xavier Oliver, v0.8
# DECLARATIONS

favColor = "Red"
luckyNumber = 42
myGPA = 3.62
myAge = 17
pineappleOnPizza = False

# If Statements -- Check for a condition to be True/False, do something if True.
if favColor == "Green":
    print("I like your style.")

if pineappleOnPizza == True:
    print("Your opinion is incorrect")    

# If-else Statement -- Check for a condition, do something for true and false
if myGPA >= 3.0:
    print("Congratulations on making the honor roll")
else:
    print("Better luck nect year. Try studying more.")

if myAge >= 18:
    print("You're an adult. Enjoy your taxes.")
else:
    print("Insolent child")

# If - elif - else Statements -- Checks for multiple conditions
if myAge >  65:
    print("Congratulations on retiring")
elif myAge > 50:
    print("Congratulations, you have earned a bonus of $1000")
else:
    print("You are not old enough for a bonus")
# 1 if, 1 else, any number of elif allowed.        

# Nested if - elif - else Statements
if myAge > 15:
    print("You are eligible for a license")
    if myGPA >= 3.5:
        print("You qualify for a new car")
    elif myGPA > 2.0:
        print("You qualify for $500 off a car")
    else:
        print("You get nothing.")
else:
    print("You are not old enough to drive")    

# When doing if - elif - else statements, check for the highest value first.
if myGPA > 1.5:
    print("You are in danger of failing for the year")
elif myGPA > 2.0:
    print("You are on track to graduate")
elif myGPA > 3.0:
    print("You qualify for some scholarship money")
elif myGPA > 3.99:
    print("You qualify for Bright Futures 100 percent scholarship")
else:
    print("GPA was not calculated. Please try again.")

# While Loop -- Think "MUSICAL CHAIRS" -- Used when you do not know how many iterations you need.
# Iteration = one complete trip through a loop
x = 0
while x < 100: 
    print(f"X is currently equal to {x}")
    x += 1

while x >= 0:
    print(f"X is currently equal to {x}")
    x -= 1

# for Loop --  Think 'Go Fish', used when you know the number of iterations needed.
print("FOR LOOP STARTS HERE")
for i in range(10): # i = iterable value
    print(i)

print("EVEN OR ODD LOOP")
for i in range(101):
    print(i)
    if i % 2 == 0:
        print("That number is even")
    else:
        print("That number is odd")

# () Parentheses
# [] Square Brackets
# <> Angle Brackets
# {} Braces