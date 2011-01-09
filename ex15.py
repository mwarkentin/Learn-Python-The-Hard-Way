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

txt.close()

# print a string
print "I'll also ask you to type it again:"

# prompt the user for a file name
file_again = raw_input("> ")

# open the file that the user entered, and then assign the file object to the variable txt_again
txt_again = open(file_again)

# print the contents of the txt_again file object
print txt_again.readlines()

txt_again.close()