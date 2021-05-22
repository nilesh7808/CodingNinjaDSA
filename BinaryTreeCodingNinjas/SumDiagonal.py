def DiagonalSum(matrix,N):
    diagonal = 0
    for i in range(0,N):
        diagonal += m[i][i]
    return diagonal

T = int(input())
for i in range(0,T):
        N = int(input())
        m = [
            [1, 2, 3, 4],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [1, 2, 3, 4]
        ]
        print(DiagonalSum(m,N))
