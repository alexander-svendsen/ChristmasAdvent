def generate_times_table(n):
    times_table_dict = {}
    for x in xrange(1, n + 1):
        for y in xrange(1, n + 1):
            times_table_dict[x * y] = 1
    return times_table_dict
 
print len(generate_times_table(8000))