#!/usr/bin/env python

priority = [  
    ['<','<','<','<','>','','<'],   # +  
    ['<','<','<','<','>','','<'],   # -  
    ['>','>','<','<','>','','<'],   # *  
    ['>','>','<','<','>','','<'],   # /  
    ['>','>','>','>','>','','>'],   # (  
    ['<','<','<','<','=','', ''],   # ) 
    ['>','>','>','>','>','', '']    # --
]    #+   -   *   /   (   )  --

# '--' is negative   '-' is minus

opindex = {'+':0, '-':1, '*':2, '/':3, '(':4, ')':5, "--":6}

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
    lastc = 1 #for recognize negative and minus
    while i < len(expression):
        operand = ""
        while (i < len(expression)) and (expression[i] not in opindex):
            operand += expression[i]
            i += 1
        if operand != "":
            operandstack.append(float(operand))
            lastc = 0
        while i < len(expression):
            if not operatorstack \
               or (compare_priority(expression[i], operatorstack[-1]) == ">"):
                if expression[i] == "-" and lastc == 1:
                    operatorstack.append("--")
                else:
                    operatorstack.append(expression[i])
                if expression[i] == "(":
                    lastc = 1
                break
            elif compare_priority(expression[i], operatorstack[-1]) == "<":
                opr1 = operandstack.pop()
                op = operatorstack.pop()
                if op == "--":
                    operandstack.append(-opr1)
                else:
                    opr2 = operandstack.pop()
                    result = operation(opr1, opr2, op)
                    operandstack.append(result)
            elif compare_priority(expression[i], operatorstack[-1]) == "=":
                operatorstack.pop()
                break
        i += 1
    while operatorstack:
        opr1 = operandstack.pop()
        op = operatorstack.pop()
        if op == "--":
            operandstack.append(-opr1)
        else:
            opr2 = operandstack.pop()
            result = operation(opr1, opr2, op)
            operandstack.append(result)
    return operandstack.pop()
if __name__ == "__main__":
    expre = "(1-(4+5+2)-3)+(-(6-3)+8)"
    print cal(expre)
    










            
