from sys import argv

try:  # https://docs.python.org/3/whatsnew/3.0.html#builtins
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

script, first_name, last_name = argv

middle_name = raw_input("What is your middle name? ")

print "Your full name is %s %s %s." % (first_name, middle_name, last_name)
