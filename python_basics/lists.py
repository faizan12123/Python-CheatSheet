# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
# Use a constructor
numbers2 = list((1,2,3,4,5))

# get a value by index
print(fruits[1])

# Get the length of the list
print(len(fruits))

# Append to the list
fruits.append('Mangoes')
print(fruits)

# Remove from list
fruits.remove('Grapes')
print(fruits)

# Insert by index
fruits.insert(2, 'Strawberries')
print(fruits)

# Change Value
fruits[0] = 'Blueberries'
print(fruits)

# Remove with pop
fruits.pop(2)
print(fruits)

# Reverse List
fruits.reverse()
print(fruits)

# Sort lists
fruits.sort() #alphabetical order
print(fruits)

# Reverse sort
fruits.sort(reverse = True)
print(fruits)