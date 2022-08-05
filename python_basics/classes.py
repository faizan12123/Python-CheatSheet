# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create a class
class User:
    # Constructor (a function that runs when u instantiate an object from a class)
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # methods 
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self): 
        self.age += 1


# Init user object
faizan = User('Faizan Hussain', 'faizan@gmail.com', 21)

print(faizan.name)
faizan.has_birthday()
print(faizan.greeting())


# Extend class (pass in the class that is being extended as a param)
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    # methods
    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# Init customer object
janet = Customer('Janet Johnson', 'janet@gmail.com', 25)

janet.set_balance(500)
print(janet.greeting())
