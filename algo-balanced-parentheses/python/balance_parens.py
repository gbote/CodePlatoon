def balance_parens(str):
    noKeep = set()
    parenIndexStack = []
    for i in range(len(str)):
        if str[i] == '(':
            parenIndexStack.append(i)
        elif str[i] == ')':
            if not parenIndexStack:
                noKeep.add(i)
            else:
                parenIndexStack.pop()

    for i in parenIndexStack:
        noKeep.add(i)

    return ''.join(str[i] for i in range(len(str)) if i not in noKeep)
