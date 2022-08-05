# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get info from file
print(f'Name: {myFile.name}')
print(f'Is closed: {myFile.closed}') # checking to see if the file is closed within our script, not our system
print(f'Opening Mode: {myFile.mode}')

# Write to file
myFile.write('I love Python')
myFile.write(' and Javascript.')
myFile.close()

# Append to the file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read from a file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100) #reads 100 characters
print(text)

# Delete a file
# import os
# os.remove("myfile.txt")
