import re
x= 'My 2 favourite numbers are 11 and 8'
y=re.findall('[0-9]+',x) #one or more digits from x
print(y)
y=re.findall('[aeiou]+',x) #one or more lowercase vowels
print(y)

