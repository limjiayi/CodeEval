# Created by JiaYi Lim on 25/12/2013

import sys, time

def ugly(num):
    '''A number is ugly if it is divisible by any of the single-digit primes
       Return 1 if a number is ugly, else return 0'''
    primes = [2,3,5,7]
    for p in primes:
        if num % p == 0:
            return 1
    return 0

def permute(string):
    '''Get all the permutations of the string by inserting + and - signs between the digits'''
    if len(string) == 1:
        return string
    else:
        perms = set()
        for i in range(1, len(string)):
            variants = permute(string[i:])
            for variant in variants:
                perms.add(string[:i] + variant)
                for op in '+-':
                    perms.add(string[:i] + op + variant)
        return perms

def evaluate(expr):
    '''Tokenize the expression and return the result'''
    tokens = []
    number = ''
    for c in expr:
        if c in '0123456789':
            number += c
        elif c == '-':
            # whenever the minus sign is encountered, make the token next to it negative
            # this allows us to use sum() to evaluate the expression
            tokens.append(int(number))
            number = '-'
        else:
            # ignore + signs
            tokens.append(int(number))
            number = ''
    tokens.append(int(number))
    return(sum(tokens))

def count_ugly():
    '''Count the number of expressions that evaluate to an ugly number'''
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.strip('\n')
            line = ''.join([ c for c in line if c != '0' ])
            permutations = permute(line)
            evaluations = [ evaluate(p) for p in permutations ]
            judgements = [ ugly(e) for e in evaluations ]
            print sum(judgements)


if __name__ == '__main__':
    count_ugly()
