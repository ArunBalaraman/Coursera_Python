txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
	t.append((len(word), word))
t.sort(reverse=True)
print t
res = list()
for length, word in t:
	res.append(word)
print res
