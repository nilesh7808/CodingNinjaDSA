def reverseStack(s1, s2):
    if len(s1) <= 1:
        return
    while len(s1) != 1:
        data = s1.pop()
        s2.append(data)
    x = s1.pop()
    while len(s2) != 0:
        data = s2.pop()
        s1.append(data)
    reverseStack(s1,s2)
    x = s1.append(x)
    pass

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
s1 = [int(ele) for ele in input().split()]
s2 = []
reverseStack(s1, s2)
while (len(s1) != 0):
    print(s1.pop(), end=' ')




