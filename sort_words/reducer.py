import sys

sorted_words = []
for line in sys.stdin :
    word = (line.strip()).split()
    
    sorted_words.append(word)
sorted_words = sorted(sorted_words)

for word in sorted_words :
    print(type(word))