from sys import argv

script, filename = argv

target = open(filename, 'w+') # http://www.manpagez.com/man/3/fopen/

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Here's your file %s:" % filename
target.seek(0) # rewind to beginning of file
print target.read()

target.close()