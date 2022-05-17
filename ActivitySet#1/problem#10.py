# Dictionaries

fname = input("Enter file name: ")
fh = open(fname)
words=list()

counts = dict()
for line in fh :
    if line.startswith("From:") :
        words = line.split()
        if words[1] not in counts:
            counts[words[1]]=1
        else:
            counts[words[1]]+=1

wo=counts.values()
z=max(wo)
for key in counts:
    if counts[key]==z:
      print(key,z)
