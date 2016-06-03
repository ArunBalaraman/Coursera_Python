import urllib
import xml.etree.ElementTree as ET

while True:
    url = raw_input('Enter location: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    data = urllib.urlopen(url).read()
    print 'Retrieved',len(data),'characters'
    tree = ET.fromstring(data)
	
    counts = tree.findall('.//count')

    total = 0
    for nmbr in counts:
		x = int(nmbr.text)
		print x
		total = total + x
	
    print 'Count:', len(counts)
    print 'Sum', total