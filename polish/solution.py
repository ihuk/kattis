#!/usr/bin/python

import sys


def main():
    operators = ['+', '-', '*', '/']
    for case, expression in enumerate(sys.stdin):
        stack = []
        terms = expression.split()
        while terms:
            term = terms.pop()
            if term in operators:
                first = stack.pop()
                second = stack.pop()
                try:
                    a = int(first)
                    b = int(second)
                    if '+' == term:
                        r = a + b
                    elif '-' == term:
                        r = a - b
                    elif '*' == term:
                        r = a * b
                    elif '/' == term:
                        r = a / b
                    stack.append(str(r))
                except Exception:
                    stack.append('{} {} {}'.format(term, first, second))
            else:
                stack.append(term)
        print 'Case {}: {}'.format(case + 1, ' '.join(stack))


if '__main__' == __name__:
    main()
