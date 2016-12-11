from sys import argv

script,filename=argv

print "we are going to eraser file %r" %filename

target = open(filename,'w+')

print "Truncate the file %r"%filename
target.truncate()


print "Now , input three lines to write a new file"
line1=raw_input("line1:")
line2=raw_input("line2:")
line3=raw_input("line3:")

print "\nNow,I'm going to write these three lines to the file"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "\nFinally,we close it"
target.close()
