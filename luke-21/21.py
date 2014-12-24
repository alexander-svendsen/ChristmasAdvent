def ascii_sum(word):
	tot = 0
	for char in word:		
		tot += ord(char)
	return tot

l = []
with open("words.txt") as f:
	for word in f.readlines():
		l.append(ascii_sum(word.rstrip()))

print sum(sorted(l)[-42::])

