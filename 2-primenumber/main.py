# -*- coding: utf-8 -*-
import math


def is_prime(num):
    # http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    for j in range(2, int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True

two_digit_primes = [str(x) for x in range(11, 99, 2) if is_prime(x)]


def find_first_digit_match(str_digit):
    for index, str_prime in enumerate(two_digit_primes):
        if str_prime.startswith(str_digit):
            return index, str_prime
    raise Exception("Not solvable")


def get_first_digit_match(str_digit):
    index, str_prime = find_first_digit_match(str_digit)
    del two_digit_primes[index]
    return str_prime


def main():
    n = 9
    m = str(n)
    while len(m) != n:
        str_prime = get_first_digit_match(m[-1])
        m += str_prime[-1]

    print m

if __name__ == "__main__":
    main()