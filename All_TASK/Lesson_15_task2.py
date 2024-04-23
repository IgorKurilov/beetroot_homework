class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * Dog.age_factor

# Example usage:
dog_age = 5
dog = Dog(dog_age)
human_equivalent_age = dog.human_age()
print(f"The dog's age in human equivalent is {human_equivalent_age} years")