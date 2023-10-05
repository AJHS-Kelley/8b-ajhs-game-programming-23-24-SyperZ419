# Data Types and Operators, Xavier Oliver, v0.8

# Variable Rules
# CANNOT START WITH A NUMBER
# CANNOT USE BUILT-IN KEYWORDS AS VARIABLES.
# VARIABLE NAME SHOULD DESCRIBE THE DATA BEING STORED.
# snake_case variables use _ to separate words, all lowercase.
# camelCase variables do not use spaces, 1st word lower, rest upper.

# String Literal Examples
playerName = "John Jaeger"
emptyString = ""
spaceString = " "
deathLocation = "Eiffel Tower"
favColor = "Blue"

# Integer Data Types
health = 100
extraLives = 5
temp = -17
usoppFans = 0

# Floating Point Data Types
pi = 3.1415678
lapTime = 3.5
velocity = -2.0
chopperBounty = 100.50

# Boolean Data Types
isFireType = False
weaponEquipped = True
pvpEnabled = False
luffyGod = True

# Arithmetic Operators
# PEMDAS APPLIES JUST LIKE IN MATH CLASS
print(4 + 3) # Addition
print(26 - 47) # Subtraction
print(3 * -4) # Multiplication
print(60 / 12) # Division
print(6 ** 12) # Exponents
print(82 % 9) # Modulus, divides 2 numbers and gives remainder

# Comparison Operators
# Evaluate the expression, then return True or False
print(6 > 4) # Greater Than
print(8 >= 7) # Greater Than or Equal To
print(1 < 7) # Less Than
print(-30 <= -300) # Less Than or Equal To
print(20 == 200) # Is Equal To
print(67 != 56) # Is Not Equal To

# Assignment Operators
myVariable = "value" # Assign variable on the left with the value on the right, throw out any current value
myVariable2 = (5 + 6)

myVariable3 = 2
myVariable3 = 7
print(myVariable3)

# Addition Assignment -- Adds the value on the right, keeping any current value
myWallet = 0
myWallet += 1
myWallet += 5
print(myWallet)

# Same Effect
x = 0
x += 1
x = x + 1

# Logical Operators
print(3 > 5 and 4 < 3) # and; requires all expressions to be true
print(3 > 2 and 4 < 3) #false
print(3 > 2 and 4 != 3) #true
print(3 > 2 and 4 != 3 and favColor == "Blue" and temp == -5)
# When writing and expressions, put the value most likely to be False first!

# Logical OR -- Requires ONE expression to be true
print(5 > 2 or 2 < -2)
print(3 != 3 or 5 == 5)

# AND OR Combination
print(3 > 2 and 4 < 3 or 5 != 7)

# NOT Logical Operator -- takes the opposite
print(not (3 > 2))
print(not (not (not (5 != 3))))

