# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 50


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x > y:
    print(f'{x} is greater than {y}')
    
# if/else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

# Else if
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
     print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')


# Nested if statements
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

# Logical operators (and, or, not) - Used to combine conditional statements

# for "and" both conditionals have to be true in order to run
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# for "or" only one conditional needs to be true in order to run
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than or equal to 10')

# not
if not (x ==y):
    print(f'{x} is not equal to {y}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

# in
if 3 in numbers:
    print(3 in numbers)

# not in
if 7 not in numbers:
    print(7 not in numbers)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:


# is
if 5 is 5:
    print(5 is 5)

# is Not
if 5 is not 4:
    print(5 is not 4)