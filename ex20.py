# import argv from sys
from sys import argv

# get arguments
script, input_file = argv

# define print_all function, which takes 1 argument (f)
def print_all(f):
    # print the contents of f
    print f.read()

# define the rewind function, which takes 1 argument (f)    
def rewind(f):
    # move the file pointer back to the beginning of file f
    f.seek(0)

# define the print_a_line function, which takes 2 arguments (line_count, f)    
def print_a_line(line_count, f):
    # print line_count, then a line from file f
    print line_count, f.readline()

# set current_file variable to a file pointer to input_file    
current_file = open(input_file)

# print string
print "First let's print the whole file:\n"

# call print_all function with current_file as an argument
print_all(current_file)

# print string
print "Now let's rewind, kind of like a tape."

# call rewind function with current_file as an argument
rewind(current_file)

# print string
print "Let's print three lines:"

# set current_line to 1
current_line = 1
# call print_a_line function with current_line and current_file as arguments
print_a_line(current_line, current_file)

# set current line to itself + 1
current_line += 1
# call print_a_line function with current_line and current_file as arguments
print_a_line(current_line, current_file)

# set current line to itself + 1
current_line += 1
# call print_a_line function with current_line and current_file as arguments
print_a_line(current_line, current_file)