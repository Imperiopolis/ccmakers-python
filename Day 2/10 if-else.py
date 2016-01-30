from sys import exit

def promptNumber(string):
	print string
	return int(raw_input('> '))

people   = promptNumber('How many people are there?')
balloons = promptNumber('How many balloons are there?')
cupcakes = promptNumber('How many cupcakes are there?')

if not people:
	print "There is nobody here?"
	exit(0)
elif not balloons and not cupcakes:
	print "This isn't going to be much of a party."
else:
	print "It looks like we have some planning to do."
	
if people is 1:
	print "You get all %d balloons and %d cupcakes to yourself!" % (balloons, cupcakes)
else:
	print "You're going to have to share."

if cupcakes < people:
	print "Some people will be sad."
elif cupcakes > 2 * people:
	print "Everyone will get seconds, and some may get thirds!"
else:
	print "Everyone gets a cupcake!"
	
if balloons >= people:
	print "Balloons for everyone!"
else:
	print "We need more balloons."

if not balloons or not cupcakes:
	print "You didn't plan your shopping list very well."