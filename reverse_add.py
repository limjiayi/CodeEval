# Created by JiaYi Lim on 25/12/2013

import sys

def palindrome(num):
    '''Return True if the number is a palindrome, else return False'''
    string = str(num)
    for i in range(len(string)):
        if string[i] != string[-1-i]:
            return False
    return True

def reverse_digits(num):
    '''Convert the integer to a list and reverse it in place'''
    lst = [ c for c in str(num) ]
    for i in range(len(lst)/2):
        lst[i], lst[-1-i] = lst[-1-i], lst[i]
    return int(''.join(lst))

def start():
    '''Return the number of iterations required to generate a palindrome'''
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            num = int(line.strip())
            num_iterations = 1
            rev = reverse_digits(num)
            while True:
                result = num + rev
                if not palindrome(result):
                    num = result
                    rev = reverse_digits(num)
                    num_iterations += 1
                else:
                    break
            print num_iterations, result


if __name__ == '__main__':
    start()