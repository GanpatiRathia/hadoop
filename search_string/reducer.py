import sys

line_number = []
lines = 1
for line in sys.stdin :
    line = line.strip()
    word,count = line.split('\t')

    if word == 'Rahul' :
        line_number.append(lines) 
    lines += 1

print('Found at locations' + str(line_number) )        