#!/usr/bin/python
import sys

def main():
    group = []
    for line in sys.stdin:
        line = line.strip()
        if 0 == len(line):
            sort(group)
            group = []
            print ''
            continue
        group.append(line)
    sort(group)


def sort(group):
    max_len = 0
    result = []
    for word in group:
        max_len = max(max_len, len(word))
        result.append(''.join(reversed(word)))
    for drow in sorted(result):
        print '{}{}'.format(' ' * (max_len - len(drow)), ''.join(reversed(drow)))


if '__main__' == __name__:
    main()

