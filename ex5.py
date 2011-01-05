name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_in_cm = height * 2.54
weight = 180 # lbs
weight_in_kg = weight * 0.45359237
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r inches tall (%r cm)." % (height, height_in_cm)
print "He's %r pounds heavy (%r kg)." % (weight, weight_in_kg)
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
	age, height, weight, age + height + weight)
	
# All formatting characters: %d, %i, %o, %u, %x, %X, %e, %E, %f, %F, %g, %G, %c, %r, %s