# create a variable called formatter, which is a string made of 4 formatting characters
formatter = "%r %r %r %r"

# prints formatter with 4 digits
print formatter % (1, 2, 3, 4)
# prints formatter with 4 strings
print formatter % ("one", "two", "three", "four")
# prints formatter with 4 Booleans
print formatter % (True, False, False, True)
# prints formatter with itself, 4 times
print formatter % (formatter, formatter, formatter, formatter)
# prints formatter with 4 strings
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# It uses both double and single quotes because one of the lines has an apostrophe in it