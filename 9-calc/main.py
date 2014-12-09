from itertools import permutations


possible = [int(''.join(p)) for p in permutations('0123456789', 3) if p[0] != '0']


def unique(result, num1, num2):
    
	

result = 99999
for x in possible:
	for y in possible:
		sum = str(x + y)
		if len(sum) == 4:
			product_str = str(x) + str(y)
			for i in sum:
				if i in product_str:
					break
			else:
				print x,y,sum
				result = min(result, x, y)


print result