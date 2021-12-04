#In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
import re
file=open('regex_sum_1413738.txt')
numlist=list()
total=0
for line in file:
    line=line.rstrip()
    y=re.findall('[0-9]+',line)
    numlist+=y
for i in numlist:
    total+=int(i)
print(total)