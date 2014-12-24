import math


def is_prime(num):
    # http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    for j in range(2, int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True

#http://no.wikipedia.org/wiki/Perfekt_tall

biggest_p_primes = [str(2**(x-1) * ((2**x)-1)) for x in xrange(2,100) if (is_prime(x) and 2**(x-1) * ((2**x)-1) < 10000)]
print ', '.join(biggest_p_primes)