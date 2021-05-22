def missNumber(arr):
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i + 1]:
            return arr[i]

n = int(input())
arr = list(int (i) for i in input().strip().split())
arr.sort()
ans = missNumber(arr)
print(ans)

# 2nd method
def missNumber(arr):
    x = (n -1 ) + (n -2)
    y = ((n-1)*(n-2))//2
    z = x - y
    return z
    pass

n = int(input())
arr = list(int(i) for i in input().strip().split())
arr.sort()
ans = missNumber(arr)
print(ans)