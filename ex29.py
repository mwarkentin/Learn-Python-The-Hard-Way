people = 20
cats = 15
dogs = 30


if people < cats:
    print "Too many cats! The world is doomed!"
    
if people > cats:
    print "Not many cats! The world is saved!"
    
if people < dogs:
    print "The world is drooled on!"
    
if people > dogs:
    print "The world is dry!"
    

dogs += 5

if people >= dogs:
    print "People are greater than equal to dogs."
    
if people <= dogs:
    print "People are less than equal to dogs."


if people == dogs:
    print "People are dogs."
    
# Extra credit
# 1. The if statement executes the code under it if the expression is True
# 2. The code under the if needs to be indented 4 spaces so that Python knows what code is part of the if block
# 3. If the code wasn't indented, it would be executed, regardless of the Truthiness of the if statement
# 5. IF we change the initial variables, we get different print statements.