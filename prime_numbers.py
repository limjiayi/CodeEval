# Created by JiaYi Lim on 11/1/2014

import sys

def find_primes(num):
    '''Use the Sieve of Eratosthenes to find all primes up to a given number'''
    # initialize a list of primality flags
    lst = [True] * num
    # 0 and 1 are known to not be prime
    lst[0] = lst[1] = False
    # iterate over the list and find the next prime
    for i, is_prime in enumerate(lst):
        if is_prime:
            # iterate over the multiples of the found prime within the limit
            for j in range(2, (len(lst)//i)+1):
                # ensure that we also check the last multiple if it is within the limit
                if i*j <= len(lst) - 1:
                    # flag each multiple as False
                    lst[i*j] = False
    return ','.join([ str(i) for i, is_prime in enumerate(lst) if is_prime ])

def start():
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line != '':
                print find_primes(int(line))


if __name__ == '__main__':
    start()