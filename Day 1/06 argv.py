from sys import argv

script, user_name = argv
prompt = '> '

print "Hi, I'm the %s script.\nI'm going to ask you some questions about %s." % (script, user_name)
print "How old is %s?" % user_name
age = raw_input(prompt)

print """
Alright, so here is what you told me about %s.
They are %s years old. That's a lot of years.
Thanks for using the %s script.
""" % (user_name, age, script)