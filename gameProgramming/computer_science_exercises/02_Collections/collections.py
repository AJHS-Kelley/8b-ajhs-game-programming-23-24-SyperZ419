# Collections Examples, Xavier Oliver, v0.5a

# LIST -- ORDERED, CHANGEABLE, ALLOWS DUPLICATE VALUES
# breakfastFoods = ["Bacon", "Waffles", "Pancakes", "Cereal", "Milk"]
# Each item of the list is known as an ELEMENT.
# The position in the for each is the INDEX.
# The element "BACON" is at index 0.
# Python Only: index -1, it is the last item on the list.
# testScores = [95, 100, 25, 15, 27, 35]
# classGPA = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25]

# Printing Contents of a List
#print(breakfastFoods)
#print(testScores)
#print(classGPA)

# Accessing Specific List Elements -- REMEMBER FIRST ELEMENT IS INDEX 0
#print(breakfastFoods[0])
#print(testScores[0])
#print(classGPA[0])

# Accessing Last Element in Lists
#print(breakfastFoods[-1])
#print(testScores[-1])
#print(classGPA[-1])

# WYOC Access the 3rd Element in Each List
#print(breakfastFoods[2])
#print(testScores[2])
#print(classGPA[2])

# Changing Items in a List
# breakfastFoods[0] = "Sausage"
# testScores[0] = 97
# classGPA[0] = 3.57
# print(breakfastFoods[0])
# print(testScores[0])
# print(classGPA[0])
# print(breakfastFoods)
# print(testScores)
# print(classGPA)

# WYOC Change 5th Element in Each List
# breakfastFoods[4] = "Orange Juice"
# testScores[4] = 50
# classGPA[4] = 4.30
# print(breakfastFoods[4])
# print(testScores[4])
# print(classGPA[4])
# print(breakfastFoods)
# print(testScores)
# print(classGPA)

# Adding and Inserting Items to a List
# .append() adds an item to the END of a list
# breakfastFoods.append("Hash Browns")
# print(breakfastFoods)
# testScores.append(99)
# print(testScores)
# classGPA.append(1.99)
# print(classGPA)

# .insert() allows you to place an item at a specific index in the list.
# breakfastFoods.insert(3, "Parfait")
# print(breakfastFoods)
# testScores.insert(3, 55)
# print(testScores)
# classGPA.insert(3, 0.0)
# print(classGPA)

# WYOC Appending to Lists
# print("APPENDS")
# breakfastFoods.append("Eggs")
# print(breakfastFoods)
# testScores.append(85)
# print(testScores)
# classGPA.append(1.24)
# print(classGPA)

# WYOC Inserting to Index 5
# print("INSERTS")
# breakfastFoods.insert(5, "Omelette")
# print(breakfastFoods)
# testScores.insert(5, 72)
# print(testScores)
# classGPA.insert(5, 1.62)
# print(classGPA)

# Deleting Items from a List
# Use .remove() to remove a specific item from the list.
# breakfastFoods.remove("Waffles")
# print(breakfastFoods)
# testScores.remove(100)
# print(testScores)
# classGPA.remove(2.25)
# print(classGPA)

# To delete using the index value we use .pop()
# breakfastFoods.pop(4)
# print(breakfastFoods)
# testScores.pop(4)
# print(testScores)
# classGPA.pop(4)
# print(classGPA)

# WYOC .pop 2nd element from each list
# print("Removal by Index")
# breakfastFoods.pop(2)
# print(breakfastFoods)
# testScores.pop(2)
# print(testScores)
# classGPA.pop(2)
# print(classGPA)

# WYOC .remove any item from the list
# print("Removal by Item")
# breakfastFoods.remove("Cereal")
# print(breakfastFoods)
# testScores.remove(27)
# print(testScores)
# classGPA.remove(1.99)
# print(classGPA)

# Determining List Length
# print(f"There are {len(breakfastFoods)} items in the breakfastFoods list.")
# WYOC List Length
# print(f"There are {len(testScores)} items in the testScores list.")
# print(f"There are {len(classGPA)} items in the classGPA list.")

# List Methods -- Functions for working with lists. 
# Sorting Lists -- Alphanumerical -- Ascending -- Capital Letters before Lower Case Letters
# print(f"The original breakfastFoods list is {breakfastFoods}.")
# breakfastFoods.sort()
# print(f"The sorted breakfastFoods list is {breakfastFoods}.")

# WYOC Sorting Lists
# print(f"The original testScores list is {testScores}.")
# testScores.sort()
# print(f"The sorted testScores list is {testScores}.")

# print(f"The original classGPA list is {classGPA}.")
# classGPA.sort()
# print(f"The sorted classGPA list is {classGPA}.")

breakfastFoods = ["Bacon", "Waffles", "Pancakes", "Cereal", "Milk", "Pancakes"]
testScores = [95, 100, 25, 15, 27, 35, 27]
classGPA = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25, 1.74]

# .count() will return the number of times a value appears in a list
# numWaffles = breakfastFoods.count("Waffles")
# print(f"There are {numWaffles} Waffles in the list.")
# numPancakes = breakfastFoods.count("Pancakes")
# print(f"There are {numPancakes} Pancakes in the list.")

# WYOC Counting Lists
# num35 = testScores.count(35)
# print(f"There are {num35} 35s in the list.")
# num27 = testScores.count(27)
# print(f"There are {num27} 27s in the list.")

# num099 = classGPA.count(0.99)
# print(f"There are {num099} 0.99s in the list.")
# num174 = classGPA.count(1.74)
# print(f"There are {num174} 1.74s in the list.")

# Deleting All Contents of a List -- .clear()
# breakfastFoods.clear()
# print(f"The breakfast foods list is {breakfastFoods}.")
# testScores.clear()
# print(f"The test scores list is {testScores}.")
# classGPA.clear()
# print(f"The class GPA list is {classGPA}.")

# Common Bugs -- Index out of Range
print(f"The last item in the list is {breakfastFoods[5]}.")

print(f"The last item in the testScores list is {testScores[len(testScores) - 1]}.")
