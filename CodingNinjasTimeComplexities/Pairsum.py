def PairSum(arr,x):
    n = len(arr)
    i = 0
    j = len(arr)-1
    while i < j:
        if arr[i] + arr[j] == x:
            






n = int(input())
arr = list(int(i) for i in input().split())
arr.sort()
x = int(input())
print(PairSum(arr,x))