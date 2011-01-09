from sys import argv

script, filename = argv

def read_file(filename):
    f = open(filename)
    print f.read()
    
read_file(filename)
read_file(raw_input("Enter a filename: "))
read_file("copied.txt")

filename = "ex1.py"
read_file(filename)