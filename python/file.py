#!/usr/bin/python

fo = open("foo.txt","wb")
print "Name of the file:", fo.name
print "File is Closed or not:", fo.closed
print "Opening mode:", fo.mode
fo.write("Hello,world!")
fo.close()
