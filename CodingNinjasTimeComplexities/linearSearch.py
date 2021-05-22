def Linear_Search(arr,x):
    if len(arr) == 0:
        return
    if arr[0] == x:
        return True
    smallerOut = Linear_Search(arr[1:],x)
    if smallerOut:
        return True
    else:
        return False


n = int(input())
arr = list(int (i) for i in input().strip().split())
x = int(input())
if Linear_Search(arr,x) :
    print("Found ")
else:
    print("Not Found ")