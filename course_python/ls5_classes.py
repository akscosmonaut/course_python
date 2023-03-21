import random

class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.word = "gav"

    def sit(self, sex):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

    def say(self):
        dog_dictionary = ["hey", "eat", "sleep"]
        self.word = random.choice(dog_dictionary)


