def printIntersection(a, b, n, m):
    i = 0
    j = 0
    x = []
    while( i < n and  j < m):
        if (a[i] == b[j]) and (i == 0 or a[i] != a[i-1]):
            x.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
    if len(x) == 0:
        x.append(-1)

    return x
m, n = map(int, input().strip().split())
print(m,n)
a = list(int (i) for i in input().strip().split())
b = list(int (i) for i in input().strip().split())
l = printIntersection(a, b, m,n)
print(*l)