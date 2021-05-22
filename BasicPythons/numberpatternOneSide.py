def pattern():
    for i in range(1,N):
        for j in range(1,N):
            if j <= i:
                print(j,end=" ")

            else:
                print(" ",end=" ")
        print()
N = int(input())
pattern()