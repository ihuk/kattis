#!/usr/bin/python

def main():
    programs = int(raw_input())
    for _ in range(programs):
        stack = []
        instructions = int(raw_input())
        for _ in range(instructions):
            instr = raw_input()
            if 'PUSH' == instr:
                stack.append(0)
            if 'DUP' == instr:
                s = stack.pop()
                stack.append(s)
                stack.append(s)
            if 'UNION' == instr:
                first = stack.pop()
                second = stack.pop()
                stack.append(first | second)
            if 'INTERSECT' == instr:
                first = stack.pop()
                second = stack.pop()
                stack.append(first & second)
            if 'ADD' == instr:
                first = stack.pop()
                second = stack.pop()
                cf = bin(first).count('1')
                cs = bin(second).count('1')
                print 'first {}, cf {}, second {}, cs {}, result {}'.format(first, cf, second, cs, second | (1 << cf << first))
                second |= (1 << cf << first)
                stack.append(second)
            print bin(stack[-1]).count('1')
        print '***'

if '__main__' == __name__:
    main()
