def is_the_number_n(number):
	divider = 10
	while divider < number:
		right_side = number % divider
		left_side = number / divider
		
		if (left_side + right_side) ** 2 == number:
			return True
		
		divider *= 10
		
	return False

print len([x for x in xrange(1, 1000000) if is_the_number_n(x)])
