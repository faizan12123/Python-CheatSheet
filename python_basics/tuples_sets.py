# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
print (fruits, fruits2)

# Single value needs trailing comma. Without the comma, data type will not be seen as a tuple
fruits3 = ('Apples',)
print(fruits3, type(fruits3))

# Get values from a tuple
print(fruits[1])

# Delete tuples
del fruits2
# print(fruits2)

# Get length
print(len(fruits))




# A Set is a collection which is unordered and unindexed. No duplicate members.


#create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to a set
fruits_set.add('Grape')
print(fruits_set)

# Remove from set
fruits_set.remove('Grape')
print(fruits_set)

# Add duplicate
fruits.set.add('Apples')
print(fruits_set)

# Clear set
fruits_set.clear()
print(fruits_set)

# Delete set
del fruits_set
# print(fruits_set)

