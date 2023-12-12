# Object-Oriented Programming, Xavier Oliver, v0.3
class Person: # Use PascalCase for ClassNames
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.weakness = None
        self.nemesis = None
    
    # To string function --> how object appears as a string
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight} pounds.\n"

    def classFunction(self):
        print("This is an example class function.\n")
        print("It only works when called on an object of that class.")

person1 = Person("Guts", 24, 254)
# print(person1)

person2 = Person("Naoki Kashima", 18, 185.5)
# print(person2)

# if person1.weight > person2.weight:
#     print(f"{person1.name} weighs more than {person2.name}.")
# elif person1.weight == person2.weight:
#     print(f"{person1.name} weighs the same as {person2.name}.")
# else:
#     print(f"{person1.name} weighs less than {person2.name}.")

# if person1.age > person2.age:
#     print(f"{person1.name} is older than {person2.name}.")
# elif person1.age == person2.age:
#     print(f"{person1.name} is the same age as {person2.name}.")
# else:
#     print(f"{person1.name} is younger than {person2.name}.")

# person1.classFunction()

# Changing properties after creation
print(person1.name)
person1.age = "25"
print(person1.name)

# Deleting Properties
# This does not 'reset' a property, it deletes it completely
print(person1.name)
del person1.weight
# print(person1)

# Deleting Objects -- Delete them if you're finished with them
del person1

# Adding Properties to Objects
person2.weakness = "Gold Kryptonite"
print(person2)
print(person2.weakness)
