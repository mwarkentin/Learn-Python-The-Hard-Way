from sys import argv

script, first_name, last_name = argv

middle_name = raw_input("What is your middle name? ")

print "Your full name is %s %s %s." % (first_name, middle_name, last_name)