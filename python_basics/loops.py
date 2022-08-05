# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
    print(f'Current Person: {person}')

# Break out of a loop
for person in people:
    if person is 'Sara':
        break
    print(f'Current Person: {person}')

# Continue (skips the current index that continue is called on; therefore skipping Sara)
for person in people:
    if person is 'Sara':
        continue
    print(f'Current Person: {person}')


# Range
for i in range(len(people)):
    # now we have to reference the current iteration by the list's index
    print(people[i])

for i in range(0,11):
    print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(f'Count: {count}')
    count +=1