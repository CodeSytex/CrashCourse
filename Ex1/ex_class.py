class Dog:
    """A simple attempt to model a dog."""

    def __init__(self):
        """Initialize name and age attributes."""

    def sit(self, name):
        """Simulate a dog sitting in response to a command."""
        print(f"{name} is now sitting.")

    #def roll_over(self, name):
    #    """"Simulate rolling over in response to a command."""
    #    print(f"{name} rolled over!")


my_dog = Dog()
my_dog.sit('Bob')

filename = 'pi_digits.txt' 
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

try:
    print(5/0)
except ZeroDivisionError:
    print("Error divide")
