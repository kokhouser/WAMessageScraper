import sys
import string
import operator
f = sys.stdin.readlines()
common = []
with open("common.txt") as something:
    for line in something:
        common.append(line.strip())
common.append("omitted>")
common.append("<media")
words = {}
for line in f:
    message = (line.split ('-'))
    del message[0]
    message = ' '.join(message)
    message = message.strip()
    # stripping first colon
    unwantedIndex = message.find(':')
    message = message[(unwantedIndex+2):]
    message = message.split(' ')
    for indiv in message:
        exclude = set(['\"', '.', '?', '!', ','])
        indiv = indiv.lower()
        indiv = list(indiv)
        indiv = ''.join(ch for ch in indiv if ch not in exclude)
        if not(indiv in common):
            indiv = indiv.capitalize()
            if (indiv in words.keys()):
                words[indiv] += 1
            else:
                words[indiv] = 1
sorted_x = sorted(words.items(), key=operator.itemgetter(1),reverse = True)
for word in sorted_x:
    print (word)
    
    