def Solve(n):
    arr = []
    for i in range(1,n):
        if n % i == 0 :
            arr.append(i)
    sum = 0
    for i in range(0,len(arr)):
        sum = sum + arr[i]
    if sum == n:
        print("YES")
    else:
        print("NO")
n = int(input())
Solve(n)