# import argv from the sys module
from sys import argv

# set script and filename variables from the script arguments
script, filename = argv

# open the filename passed in as an argument, and assign the file object to the txt variable
txt = open(filename)

# print a string with the filename
print "Here's your file %r:" % filename

# print the contexts of the txt file object
print txt.read()