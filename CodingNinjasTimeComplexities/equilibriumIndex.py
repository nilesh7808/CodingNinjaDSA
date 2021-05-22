def equilibriumIndex(arr):
    ts = 0
    i = 0
    while i < len(arr):
        ts = ts + arr[i]
        i += 1

    ls = 0
    index = 0
    while index < len(arr):
        rs = ts - ls - arr[index]
        if rs == ls:
            return index
        ls = ls + arr[index]
        index += 1
    return -1

n = int(input())
arr = list(int (i) for i in input().strip().split())
print(equilibriumIndex(arr))