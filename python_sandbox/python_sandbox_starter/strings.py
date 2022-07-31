# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Brad"
age = 37

#concatenate
print("Hello, my name is " + name + " and I am " + str(age)) #can only concatenate strings together so int can not be concatenated to the 


# String Formatting

# arguments by position
print('Hello, my name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (python 3.6+)
print(f'Hello, my name is {name} and I am {age}')


# String Methods

s = 'hello world'
t = "tester Yoyo"

#capitalize first letter of string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(t.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric (s is false because of the space between "Hello World")
print(s.isalnum())

# Is all alphabetic (s is false because of the space between "Hello World")
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
