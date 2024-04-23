class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print("Woof Woof")

class Cat(Animal):
    def talk(self):
        print("Meow")

def make_animal_talk(animal):
    animal.talk()

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the talk method on instances
make_animal_talk(dog)  # Output: Woof Woof
make_animal_talk(cat)  # Output: Meow
