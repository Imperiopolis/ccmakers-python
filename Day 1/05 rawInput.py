prompt = "> "
print "What is your name?"
name   = raw_input(prompt)
print "What is your age?"
age    = raw_input(prompt)
print "What is your height?"
height = raw_input(prompt)
print "What color are your eyes?"
eyes   = raw_input(prompt)
print "What color is your hair?"
hair   = raw_input(prompt)

print "Let's talk about %s." % name
print "They're %r years old." % age
print "They're %r tall, but I don't know the units." % height
print "They've got %s eyes and %s hair." % (eyes, hair)

# what is this doing?
print "If I add %r and %r I get %r." % (
    age, height, age + height)