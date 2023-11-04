

class Cat:    #always assign a class that you want to store 
 
    species = "Feline"

    def __init__(self, name, age):
        self.name = name 
        self.age =  age
        self.paws = "Four paws"

#instance method
    def description(self):
         return f"{self.name} is {self.age} years old"

#instance method
    def speak(self, sound):
        return f"{self.name} meows: {sound}"
    
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}, you are now {self.age} years old")

#creating the object of the class
kitten = Cat("Felix", 2)
ginger_kitten = Cat("Ginger", 3)

#to access the object's attributes
print(kitten.name)
print(kitten.age)

#call objects methods
print(kitten.description)
kitten.birthday()
print(kitten.speak("Meow Meow"))