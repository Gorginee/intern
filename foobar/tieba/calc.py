# -*- coding:utf-8 -*-

from functools import reduce


def calc(*args, operator='+'):
    if operator == '+':
        return reduce(lambda x, y: x+y, args)
    elif operator == '-':
        return reduce(lambda x, y: x-y, args)
    elif operator == '*':
        return reduce(lambda x, y: x*y, args)
    else:
        return reduce(lambda x, y: x/y, args)


if __name__ == '__main__':
    print(calc(1, 3, 5, operator='*'))
