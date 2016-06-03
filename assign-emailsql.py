import sqlite3

conn = sqlite3.connect('pythonsql3.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input("Enter file name: ")
if len(fname) < 0 : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
	if not line.startswith("From "): continue
	words = line.split()
	word = words[1]
	index = word.find('@')
	org = word[index+1:]
	#print org
	cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
	row = cur.fetchone()
	if row is None:
		cur.execute('''INSERT INTO Counts (org, count) VALUES (?,1)''', (org, ))
	else:
		cur.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''', (org, ))
conn.commit()		
sqlstr = '''SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'''

for row in cur.execute(sqlstr):
	print str(row[0]), row[1]
	
conn.commit()
cur.close()
