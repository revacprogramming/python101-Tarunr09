# Regular Expressions
# https://www.py4e.com/lessons/regex

import re
hand = open('regex_sum1.txt')
lst = []

for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    lst = lst + x

sum=0
for z in lst:
    sum = sum + int(z)
print(sum)