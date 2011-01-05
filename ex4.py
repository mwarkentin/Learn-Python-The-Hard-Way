# We have 100 cars
cars = 100

# You can fit 4 people in a car
space_in_a_car = 4

# We have 30 drivers
drivers = 30

# We have 90 passengers
passengers = 90

# After all of the drivers are in cars, we have "cars not driven" left over
cars_not_driven = cars - drivers

# The number of cars driven equals the number of drivers
cars_driven = drivers

# Carpool capacity is the number of cars driven multiplied by the space in each car
carpool_capacity = cars_driven * space_in_a_car

# The average number of passengers in each car equals the number of passengers divided by the number of cars available
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Extra credit: The error was caused by a misspelling of carpool_capacity (car_pool_capacity)
# 4.0 is used to convert to floating point number

"""
>>> i = 40
>>> x = 234
>>> j = 23.4
>>> i * x / j
400.0
"""