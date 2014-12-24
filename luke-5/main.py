# -*- coding: utf-8 -*-
from itertools import permutations

# stole it from here http://stackoverflow.com/questions/15347174/python-finding-prime-factors
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


big_number = [int("".join(x)) for x in permutations('123456789')]


def find_smallest_biggest_prime():
    smallest_biggest_prime = 999999999
    for num in big_number:
        biggest_prime_number = largest_prime_factor(num)
        if biggest_prime_number < smallest_biggest_prime:
            smallest_biggest_prime = biggest_prime_number
    return smallest_biggest_prime


def main():
    print find_smallest_biggest_prime()

if __name__ == "__main__":
    main()