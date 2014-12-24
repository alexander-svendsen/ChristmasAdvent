
def correct_number(num):
	last_digit = num % 10
	rest = num / 10
	return int(str(last_digit) + str(rest) ) == 4 * num


number = 6
while not correct_number(number):
	number += 10

print number

