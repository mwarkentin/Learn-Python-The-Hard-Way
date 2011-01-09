# define the chees_and_crackers function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print the number of cheeses
    print "You have %d cheeeses!" % cheese_count
    # print the number of boxes of crackers
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # print a string
    print "Man that's enough for a party!"
    # print a string with a line break
    print "Get a blanket.\n"

# print a string
print "We can just give the function numbers directly:"
# pass 20, 30 to the cheese_and_crackers function
cheese_and_crackers(20, 30)

# print a string
print "OR, we can use variables from our script:"
# set a variable to 10
amount_of_cheese = 10
# set a variable to 50
amount_of_crackers = 50

# pass amount_of_cheese and amount_of_crackers variables to cheese_and_crackers function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print a string
print "We can even to math inside too:"
# pass 10 + 20 and 5 + 6 to the cheese_and_crackers function
cheese_and_crackers(10 + 20, 5 + 6)

# print a string
print "And we can combine the two, variables and math:"
# pass the amount of cheese variable + 100 and the amount_of_crackers variable + 1000 to the cheese_and_crackers function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)