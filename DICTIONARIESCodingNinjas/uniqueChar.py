def unioqueChar(S):
    newStr = ""
    for i in range(0, len(S)):
        if S[i]  not in newStr:
            newStr += S[i]
    return newStr

S = input()
print(unioqueChar(S))