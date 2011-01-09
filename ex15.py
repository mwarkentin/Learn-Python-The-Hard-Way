# print a string
print "I'll also ask you to type it again:"

# prompt the user for a file name
file_again = raw_input("> ")

# open the file that the user entered, and then assign the file object to the variable txt_again
txt_again = open(file_again)

# print the contents of the txt_again file object
print txt_again.read()