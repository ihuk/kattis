#!/usr/bin/python

def main():
    current = map(int, reversed(raw_input().split(':')))
    explosion = map(int, reversed(raw_input().split(':')))
    carry = 0
    result = []
    for c0, c1, c2 in zip(current, explosion, [60, 60, 24]):
        r = c1 - c0 - carry
        if r < 0:
            r += c2
            carry = 1
        else:
            carry = 0
        result.append(r)
    if 0 == result[2] and 0 == result[1] and 0 == result[0]:
        result = [0, 0, 24] 
    print '{:02}:{:02}:{:02}'.format(result[2], result[1], result[0])


if '__main__' == __name__:
    main()

