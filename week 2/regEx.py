#Using re.search() like find()
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if line.find('From:')>=0:
        print(line)
print(" ")

import re
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('From:',line):
        print(line)
print(" ")


#Using re.search() like startswith()
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if line.startswith('From:'):
        print(line)
print(" ")

hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('^From:',line):
        print(line)