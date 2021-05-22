def maxPathRecurs(m,n):

    #base case
    if (m == 1) or (n == 1):
        return 1

    return maxPathRecurs(m,n-1) + maxPathRecurs(n,m-1)

m = int(input())
n = int(input())
print(maxPathRecurs(m,n))