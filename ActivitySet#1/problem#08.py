# Files

fname = input("Enter file name: ")
fh = open(fname)
count = 0
x = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count +1
    z = line.find('0')
    y = float(line[z:])
    x = float(x + y)
    
average = x/count
print ("Average spam confidence:",average)
