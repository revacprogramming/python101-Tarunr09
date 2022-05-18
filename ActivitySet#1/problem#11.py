# Tuples

fname = input("Enter file name: ")
fh = open(fname)

d = dict()
for line in fh :
    if line.startswith("From ") and not line.startswith("From:"):
       words = line.split()
       a =words[5].split(':')
       b = a[0]
       d[b] = d.get(b,0) + 1

lst = list()
for k,v in d.items() :
    lst.append((k,v))
lst.sort()
for k,v in lst :
    print(k,v)