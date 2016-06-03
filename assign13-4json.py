import urllib
import json


address = raw_input("Enter Location:  ")
if len(address) < 1 : exit()
	
data = urllib.urlopen(address).read()
info = json.loads(data)

total = 0

for stuff in info["comments"]:
	x = stuff.items()
	for y in x:
		if y[0] == "count":
			total = y[1] + total
print total