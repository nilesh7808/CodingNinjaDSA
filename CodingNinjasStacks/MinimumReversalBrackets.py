def BracketRev(string):
    if len(string) == 0:
        return 0
    if len(string) % 2 != 0:
        return -1
    s = []
    for i in string:
        if i == '{':
            s.append(i)
        else:
            if (len(s) > 0 and s[-1] == '{'):
                s.pop()
            else:
                s.append(i)
    count = 0
    while len(s) != 0:
        c1 = s.pop()
        c2 = s.pop()
        if c1 != c2:
            count += 2
        else:
            count += 1
    return count
string = input()
print(BracketRev(string))