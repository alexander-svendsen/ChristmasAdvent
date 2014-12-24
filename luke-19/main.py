
def is_palindrome(string):
	return string.lower() == string.lower()[::-1]


biggest_palindrome = ""
with open("text.txt") as f:
    content = f.readlines()[0]
    for x in xrange(0, len(content)):
    	for y in xrange(x + 1, len(content)):
    		word = content[x:y]
    		if is_palindrome(word) and len(word) > len(biggest_palindrome):
    			biggest_palindrome = word


print biggest_palindrome