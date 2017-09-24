#!/usr/bin/env python

priority = [  
    ['<','<','<','<','>',''],   # +  
    ['<','<','<','<','>',''],   # -  
    ['>','>','<','<','>',''],   # *  
    ['>','>','<','<','>',''],   # /  
    ['>','>','>','>','>',''],   # (  
    ['<','<','<','<','=',''],   # )   
]    #+   -   *   /   (   )


opindex = {'+':0, '-':1, '*':2, '/':3, '(':4, ')':5}

operandstack = []
operatorstack = []

def operation(num1, num2, op):
    if op == "+":
        return num1 + num2
    if op == "-":
        return num2 - num1
    if op == "*":
        return num1 * num2
    if op == "/":
        return float(num2) / num1

def compare_priority(notation, stacktop):
        return priority[opindex[notation]][opindex[stacktop]]

def cal(expression):
    i = 0
    while i < len(expression):
        operand = ""
        while (i < len(expression)) and (expression[i] not in opindex):
            operand += expression[i]
            i += 1
        if operand != "":
            operandstack.append(float(operand))
        while i < len(expression):
            if not operatorstack:
                operatorstack.append(expression[i])
                break
            elif compare_priority(expression[i], operatorstack[-1]) == ">":
                operatorstack.append(expression[i])
                break
            elif compare_priority(expression[i], operatorstack[-1]) == "<":
                result = operation(operandstack.pop(),
                                   operandstack.pop(),operatorstack.pop())
                operandstack.append(result)
            elif compare_priority(expression[i], operatorstack[-1]) == "=":
                operatorstack.pop()
                break
        i += 1
    while operatorstack:
        result = operation(operandstack.pop(),
                           operandstack.pop(),operatorstack.pop())
        operandstack.append(result)
    return operandstack.pop()
if __name__ == "__main__":
    expre = "5*(8+7)*10"
    print cal(expre)
    










            
