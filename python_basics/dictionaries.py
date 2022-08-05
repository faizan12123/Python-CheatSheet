# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create a Dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age' : 30
}

print(person, type(person))

# Use Constructor
person2 = dict(first_name='Sara', last_name='Williams')

print(person2, type(person2))

# Get a value from the dictionary
print(person['first_name'])
print(person.get('last_name'))

# Add a key/value to dict
person['phone'] = '555-555-5555'
print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict and add to it
person3 = person.copy()
person3['city'] = 'Boston'
print(person3)

# Remove an item from dict
del(person['age'])
print(person)
person.pop('phone')
print(person)

# Get length
print(len(person))

# Clear dict
person.clear()
print(person)

# List of dictionaries
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people)
print(people[1]['name'])