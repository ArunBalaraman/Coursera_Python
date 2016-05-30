name = raw_input("Enter file:")
try:
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
except:
    print "Invalid file name"
    exit()
cts = dict()
for line in handle:
    if line == "" : continue
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()
        for word in words:
            if ":" in word:
                time = word.split(":")
                if time[0] not in cts:
                    cts[time[0]] = 1
                else:
                    cts[time[0]] = cts[time[0]] + 1
            else: continue
    else: continue
lst = list()
for key, val in cts.items():
    lst.append((key, val))
lst.sort()
for key, val in lst:
    print key, val