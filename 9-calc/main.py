from itertools import permutations


possible = [int(''.join(p)) for p in permutations('0123456789', 3) if p[0] != '0']


def is_zero_to_nine(full_string):
    return ''.join(sorted(full_string)) == '0123456789'


result = 99999
for x in possible:
    for y in possible:
        sum = str(x + y)
        if is_zero_to_nine(sum + str(x) + str(y)):
            result = min(result, x, y)

print result