prompt = "> "
print "What is your name?"
name   = raw_input(prompt)
print "What is your age?"
age    = int(raw_input(prompt))
print "What is your height?"
height = int(raw_input(prompt))
print "What color are your eyes?"
eyes   = raw_input(prompt)
print "What color is your hair?"
hair   = raw_input(prompt)

print "Let's talk about %s." % name
print "They're %d years old." % age
print "They're %d tall, but I don't know the units." % height
print "They've got %s eyes and %s hair." % (eyes, hair)

# what is this doing?
print "If I add %d and %d I get %d." % (
    age, height, age + height)