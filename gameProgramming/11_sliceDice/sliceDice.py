alphabet = "abcdefghijklmnopqrstuvwxyz"
myString = "Darkest Diablos, Lord of the Lair."

print(alphabet[0])
print(alphabet[-1])

# Slicing Strings
print(alphabet[0:6]) # Slice up to second index
print(myString[0:6])

# Slice from start
print(alphabet[:9])
print(myString[:9])

# Slice to the end
print(alphabet[15:])
print(myString[15:])

# Slice the whole thing
print(alphabet[:])
print(myString[:])

# Negative index slicing
print(alphabet[-5:])
print(myString[-5:])

print(myString[::-1])