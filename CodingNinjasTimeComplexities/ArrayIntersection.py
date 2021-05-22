def intersection(A, B):
    i = 0
    j = 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1

        elif A[i] > B[j]:
            j += 1

        else:
            print(A[i])
            i += 1
            j += 1


# Main
n1 = int(input())
A = list(int(i) for i in input().strip().split(' '))
n2 = int(input())
B = list(int(i) for i in input().strip().split(' '))
# mergeSort(A,0,n1)
# mergeSort1(B,0,n2)
A.sort()
B.sort()
intersection(A, B)