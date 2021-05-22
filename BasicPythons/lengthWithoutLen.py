def print_Length(arr):
    length = 0
    for i in arr:
        length += 1
    print(length)


arr = list(int (i) for i in input().strip().split())
print_Length(arr)