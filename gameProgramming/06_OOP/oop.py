# Object-Oriented Programming, Xavier Oliver, v0.1
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