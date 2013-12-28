# Created by JiaYi Lim on 26/12/2013

import sys

def do_math(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return 'Unsupported operator'

def eval_prefix(expr):
    ops = []
    nums = []
    for c in expr:
        if c in '+-*/':
            ops.append(c)
        elif c in '0123456789':
            nums.append(int(c))
        if len(nums) == 2:
            operator = ops.pop()
            num1 = nums.pop(0)
            num2 = nums.pop(0)
            result = do_math(num1, num2, operator)
            nums.append(result)
    return nums.pop(0)

def start():
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            expression = line.strip().split()
            print eval_prefix(expression)

if __name__ == '__main__':
    start()