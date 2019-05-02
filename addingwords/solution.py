#!/usr/bin/python

import sys


def main():
    variables = {}
    variable_values = {}
    operators = ['+', '-', '=']

    def _def(args):
        name, value = args
        if name in variables.keys():
            del variable_values[variables[name]]
        variables[name] = int(value)
        variable_values[int(value)] = name 
    
    def _calc(args):
        expression = _substitute(args)
        if 'unknown' in expression:
            print ' '.join(args), 'unknown'
        else:
            result = _evaluate(expression)
            print ' '.join(args), variable_values.get(result, 'unknown')

    def _clear(args):
        variables.clear()
        variable_values.clear()
    
    def _substitute(args):
        result = []
        for term in args:
            if term in operators:
                result.append(term)
            else:
                result.append(variables.get(term, 'unknown'))             
        return result
 
    def _evaluate(expression):
        op_stack = []
        val_stack = []
        for term in expression:
            if term in operators:
                if op_stack:
                    operator = op_stack.pop()
                    second = val_stack.pop()
                    first = val_stack.pop()
                    result = first + second if '+' == operator else first - second
                    #print '{} {} {} = {}'.format(first, operator, second, result)
                    val_stack.append(result)
                op_stack.append(term)
            else:
                val_stack.append(term)
        return val_stack.pop()
     
    ops = {
        'def': _def,
        'calc': _calc,
        'clear': _clear
    }
 
    for line in sys.stdin:
        command = line.split()
        op = command.pop(0)
        ops[op](command) 


if '__main__' == __name__:
    main()

