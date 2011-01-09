from sys import argv

script, filename = argv

f = open(filename)
print f.read()