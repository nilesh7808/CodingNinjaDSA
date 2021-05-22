# def Rotate(arr, d):
#     newarr = []
#     for i in range(len(arr)-1,-1,-1):
#         newarr = arr[i]
#     for i in range(len(newarr)-d,-1,-1):
#         newarr = newarr[i]
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))
# d=int(input())
# Rotate(arr, d)
# print(*arr)
arr = [ 1, 2, 3, 4, 5, 6 ]
d = 2
n = 6
newArr = []
for i in range(len(arr)-1,-1,-1):
    newArr = arr[i]
    print(newArr,end=" ")
for j in range(0,n-d):
    print(reversed(newArr))
# arr = arr[::d]
# print(arr)


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def Rotate(arr, d):
    # Please add your code here
    l = len(arr)
    d %= l
    reverse(arr, 0, l - 1)
    reverse(arr, 0, l - d - 1)
    reverse(arr, l - d, l - 1)


# Main
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
d = int(input())
Rotate(arr, d)
print(*arr)

