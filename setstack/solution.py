#!/usr/bin/python

empty = frozenset()

def main():
    programs = int(raw_input())
    for _ in range(programs):
        stack = []
        instructions = int(raw_input())
        for _ in range(instructions):
            instr = raw_input()
            if 'PUSH' == instr:
                stack.append(empty)
            if 'DUP' == instr:
                s = stack.pop()
                stack.append(s)
                stack.append(s)
            if 'UNION' == instr:
                first = stack.pop()
                second = stack.pop()
                stack.append(first.union(second))
            if 'INTERSECT' == instr:
                second = stack.pop()
                first = stack.pop()
                stack.append(first.intersection(second))
            if 'ADD' == instr:
                first = stack.pop()
                second = stack.pop()
                if first in second:
                    stack.append(second)
                else:
                    second = set(second)
                    second.add(first)
                    stack.append(frozenset(second))
            print len(stack[-1]) 
        print '***'

if '__main__' == __name__:
    main()
