print "What's your name?"
name = raw_input('==>')
print "How old are you?",
age = raw_input()
print "How many tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, your name is %r, you're %r old, %r tall and %r heavy." % (
    name, age, height, weight)
    
# 1. raw_input() takes input from the user, and always returns a string