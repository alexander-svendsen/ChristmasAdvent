import time
def is_zero_to_nine(full_string):
    return ''.join(sorted(full_string)) == '0123456789'


def smallest_part():
    for x in xrange(102, 987):
        for y in xrange(987, 102, -1):
            if len(str(x + y)) == 4 and is_zero_to_nine(str(x + y) + str(x) + str(y)):
                return x

print smallest_part()