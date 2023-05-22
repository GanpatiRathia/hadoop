import sys
for line in sys.stdin :
    words = (line.strip()).split()
    for word in words :
        print('%s\t%s'%(word , 1))