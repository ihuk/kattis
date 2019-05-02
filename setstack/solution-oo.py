class Computer:
    def __init__(self):
        self.stack = []

    def execute(self, instruction):
        instructions = {
            'PUSH': lambda: self._push(),
            'DUP': lambda: self._dup(),
            'UNION': lambda: self._union(),
            'INTERSECT': lambda: self._intersect(),
            'ADD': lambda: self._add()
        }
        instructions[instruction]()
        print len(self.stack[-1]) 
    
    def _push(self):
        self.stack.append(frozenset())
    
    def _dup(self):
        first = self.stack.pop()
        self.stack.append(first)
        self.stack.append(first)

    def _add(self):
        first = set(self.stack.pop())
        first.add(self.stack.pop())
        self.stack.append(frozenset(first))

    def _union(self):
        first = self.stack.pop()
        second = self.stack.pop()
        self.stack.append(first | second)

    def _intersect(self):
        first = self.stack.pop()
        second = self.stack.pop()
        self.stack.append(first & second)

def main():
    programs = int(raw_input())
    for _ in range(programs):
        computer = Computer() 
        instructions = int(raw_input())
        for _ in range(instructions):
            computer.execute(raw_input())
        print '***'

if '__main__' == __name__:
    main()
