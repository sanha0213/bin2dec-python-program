
#10 digit binary to decimal conversion python code

import sys # Command line arguments
import re # regex

# beginning of the string [01] set of characters occurs one or more times at the end of the string
# re.serach function checks whether the input is 1 or 0
# % replace

if len(sys.argv) != 2 or not re.search('^[01]+$', sys.argv[1]) :
    print "Usage %s <binary_number>" % (sys.argv[0])
    print "  Print a number in binary"
    sys.exit(-1)

b = sys.argv[1]
print "b = 0b"+b

d = 0

for i in range(len(b)):
    if b[len(b)-i-1] == "1":
        d += 2**i

print "d = "+str(d)
