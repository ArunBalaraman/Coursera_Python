import re
fname = raw_input("Please enter a file name")
hand = open(fname)
lst = list()
total = 0
for line in hand:
	if line == "" : continue
	line = line.rstrip()
	x = re.findall('\s*([0-9]+)\s*', line)
	if len(x) > 0:
		lst.append(x)
#print lst		
for nmbr in lst:
	for y in nmbr:
		total = int(y) + total
print total