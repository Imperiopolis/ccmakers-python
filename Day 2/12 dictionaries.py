# create a mapping of state to abbreviation
states = {
    'OR': 'Oregon',
    'FL': 'Florida',
    'CA': 'California',
    'NY': 'New York',
    'MI': 'Michigan' 
}

# add some more states
states['MA'] = 'Massachusetts'
states['ME'] = 'Maine'
states['Texas'] = 'TX'

# print some states
print '-' * 10
print "MA is the abbreviation for: ", states['MA']
print "MI is the abbreviation for: ", states['MI']

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (abbrev, state)

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('TX', None)

if not state:
    print "Sorry, no TX."

# get a state with a default value
name = states.get('TX', 'Does Not Exist')
print "The name for the state 'TX' is: %s" % name