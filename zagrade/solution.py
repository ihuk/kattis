#!/usr/bin/python

def main(expression=None):
    if expression is None:
        expression = raw_input()
    stack = []
    pairs = []
    for i, c in enumerate(expression):
        if '(' == c:
            stack.append(i)
        if ')' == c:
            pairs.append((stack.pop(), i))
    combinations = 2**len(pairs)
    results = set()
    for i in range(1, combinations):
        e = expression 
        removed_pairs = [pairs[index] for (index, bit) in enumerate(reversed(bin(i)[2:])) if '1' == bit]
        for start, end in removed_pairs:
            e = e[:start] + '_' + e[start + 1:end] + '_' + e[end + 1:]
        results.add(e.replace('_', ''))
    for result in sorted(results): 
        print result 

if '__main__' == __name__:
    #main('(1+(2*(3+4)))')
    main()
