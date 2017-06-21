
count = 0

def stackpoporder(str, tmp, index, stack):
    global count
    if index >= len(str) and not stack:
        print tmp
        count += 1
        return
    if stack:
        top = stack.pop()
        stackpoporder(str, tmp+top, index, stack)
        stack.append(top)
    if index < len(str):
        stack.append(str[index])
        stackpoporder(str, tmp, index+1, stack)
        stack.pop()


stack = []
stackpoporder("123456","",0,stack)
print count
