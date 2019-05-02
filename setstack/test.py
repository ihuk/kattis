def execute(infn):
    f = open(infn, 'r') 
    programs = int(f.readline())
    for _ in range(programs):
        stack = []
        instructions = int(f.readline())
        for _ in range(instructions):
            instr = f.readline()
            if 'PUSH' == instr:
                stack.append(frozenset())
            if 'DUP' == instr:
                stack.append(stack[-1])
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
                second = set(stack.pop())
                second.add(first)
                stack.append(frozenset(second))
            print stack
            print len(stack[-1]) 
        print '***'
