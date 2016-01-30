def inchesToFeet(inches):
	return inches / 12.0
	
def yearsToMonths(years):
	return years * 12

my_name = 'Nora Autumn Trapp'
my_age = 24 # years
my_height = 71 # inches

print "Let's talk about %s." % my_name
print "She's %d years old, or %d months." % (my_age, yearsToMonths(my_age))
print "She's %d inches tall, or %f feet." % (my_height, inchesToFeet(my_height))
