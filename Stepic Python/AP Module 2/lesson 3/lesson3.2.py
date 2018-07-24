import itertools
from math import factorial

def primes():
    number = 2
    while True:
        if (factorial(number - 1) + 1) % number == 0:
            yield number
        number += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
