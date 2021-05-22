def SingleLaneHighway(n,s):
    count = 0
    from itertools import permutations
    x=permutations(s)
    for i in list(x):
        count+=1
    y=count
    fact=1
    for j in range(1,n+1):
        fact*=j
    group=0
    for i in range(n):
        group+=fact/(n-i)
    print("{:.6f}".format(group/y))
n = int(input())
s = list(int(i) for i in input().split())
SingleLaneHighway(n,s)
