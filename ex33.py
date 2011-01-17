def add_numbers(max, step=1):
    i = 0
    numbers = []
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    
    return numbers

numbers = add_numbers(10, 5)

print "The numbers: "

for num in numbers:
    print num