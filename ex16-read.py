from sys import argv

script, filename = argv

print "Opening %r..." % filename
f = open(filename)

print "Printing the contents of %r..." % filename
print f.read()