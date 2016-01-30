def inchesToFeet(inches):
	print "%d inches is %f feet." % (inches, inches / 12)
	
def yearsToMonths(years):
	print "%d years is %d months." % (years, years * 12)

my_name = 'Nora Autumn Trapp'
my_age = 24 # years
my_height = 71 # inches

print "Let's talk about %s." % my_name
print "She's %d years old." % my_age
print "She's %d inches tall." % my_height
    
inchesToFeet(my_height)
yearsToMonths(my_age)
    
