# Object-Oriented Programming, Xavier Oliver, v0.2
class Person: # Use PascalCase for ClassNames
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    # To string function --> how object appears as a string
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight} pounds."


person1 = Person("Guts", 24, 254)
print(person1)

person2 = Person("Naoki Kashima", 18, 185.5)
print(person2)

if person1.weight > person2.weight:
    print(f"{person1.name} weighs more than {person2.name}.")
elif person1.weight == person2.weight:
    print(f"{person1.name} weighs the same as {person2.name}.")
else:
    print(f"{person1.name} weighs less than {person2.name}.")

if person1.age > person2.age:
    print(f"{person1.name} is older than {person2.name}.")
elif person1.age == person2.age:
    print(f"{person1.name} is the same age as {person2.name}.")
else:
    print(f"{person1.name} is younger than {person2.name}.")