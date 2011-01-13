# sets the variable "people" to 50
people = 50

# sets the variable "cars" to 60
cars = 60

# sets the variables "buses" to 50
buses = 50

# if "cars is greater than people"
if cars > people:
    # print string
    print "We should take the cars."
    
# else if "cars is less than people"
elif cars < people:
    # print string
    print "We should not take the cars."

# else
else:
    # print string
    print "We can't decide."

# if "buses greater than cars"    
if buses > cars:
    # print string
    print "That's too many buses."

# else if "buses less than cars"
elif buses < cars:
    # print string
    print "Maybe we could take the buses."
# else
else:
    print "We still can't decide."

# if "people is greater than buses"    
if people > buses:
    # print string
    print "Alright, let's just take the buses."

# else
else:
    # print string
    print "Fine, let's stay home then."
    
# Extra credit
# 1.a. elif means "else if" - if the previous "if" statement is False, python checks if this elif statement is True. If it is, the code block under it will be evaluated.
# 1.b. else means "else" - if the previious "if (or elif)" statement is False, python evaluates the code block under the "else" statement
