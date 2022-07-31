# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
#variable deceleration

x=1           #into
y= 2.5        #float
name = 'john' #str
is_cool = True #bool; First letter must be capatalized


# Multiple Assignments

x, y, name, is_cool = (1,2.5, 'john', True)

#basic Math functions

a = x+y

#print

print(x, y, name, is_cool, a)


# How to check data type

print(type(x))

#data type Casting

x = str(x)
print(type(x))

y= int(y)
print(type(y), y) #casting a float to an int will make it remove it's decimal without rounding

z = float(y)
print(type(z), z) #adds a .0 to the end of a number when turned into a float