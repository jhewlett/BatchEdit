#Justin Hewlett
#Assignment 2

import random

random.seed()

#Given a number n, applies Fermat's primality test ntrials times.
#If it passes all of the tests, returns true, false otherwise.
def is_fermat_prime(n, ntrials):
    if n <= 1:
        return False
    elif ntrials <= 0:
        return True
    else:
        a = random.randint(1, n - 1)
        return a ** n % n == a % n and is_fermat_prime(n, ntrials - 1)

#Given a list of numbers, returns a sublist of Fermat primes
#that pass the test ntrials times.
def find_fermat_primes(list, ntrials):
    if len(list) == 0:
        return []
    else:
        #test the head of the list, then recursively test the tail
        head = list[0]
        if is_fermat_prime(head, ntrials):
            return [head] + find_fermat_primes(list[1:], ntrials)
        else:
            return find_fermat_primes(list[1:], ntrials)
