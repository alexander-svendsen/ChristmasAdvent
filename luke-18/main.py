from collections import defaultdict
import operator

def get_anagrams():
    d = defaultdict(int)
    with open("words.txt") as f:
    	for word in f.readlines():
        	key = "".join(sorted(word.lower()))
        	d[key] += 1
    return d


print max(get_anagrams().iteritems(), key=operator.itemgetter(1))[0]