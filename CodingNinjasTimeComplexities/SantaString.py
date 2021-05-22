def santa_String(s):
    count = 0
    if len(s) == 0 or len(s) == 1:
        return -1
    smallerOutput = santa_String(s[1:])
    if s[0] == s[1]:
        count += 1
        return count
    else:
        return -1
s = input()
print(santa_String(s))
