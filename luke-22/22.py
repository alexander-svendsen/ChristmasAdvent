def sum_of_the_square_digits(number):
	res = 0
	while number:
		digit = number % 10
		number /= 10
		res += digit ** 2
	return res


def valid_number(number):
	previous_numbers = []
	num = sum_of_the_square_digits(number)
	while  num != 1:
		if num in previous_numbers:
			return False
		previous_numbers.append(num)
		num = sum_of_the_square_digits(num)
	return True

print [x for x in xrange(1,50) if valid_number(x)]