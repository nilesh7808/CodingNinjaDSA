
def checkBalanced(exp):
    s = []
    for i in exp:
        if i in '({[':
            s.append(i)
        elif i is ')':
            if (not s or s[-1] != '('):
                return False
            s.pop()
        elif i is '}':
            if (not s or s[-1] != '{'):
                return False
            s.pop()
        elif i is ']':
            if (not s or s[-1] != '['):
                return False
            s.pop()
    if (not s):
        return True
    return False

exp=input()
ans = checkBalanced(exp)
print(ans)
