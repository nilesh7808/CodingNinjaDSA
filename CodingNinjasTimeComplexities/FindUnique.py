def FindUnique(arr):
    x = 0
    for i in range(n):
        x = x ^ arr[i]
    return x

n = int(input())
arr = list(int (i) for i in input().strip().split())
unique = FindUnique(arr)
print(unique)