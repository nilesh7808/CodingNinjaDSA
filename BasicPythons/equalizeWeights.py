import random
N=int(input())
for i in range(N):
    G=int(input())
    W=list(int(i) for i in input().strip().split())
    sum=0
    for i in range(0,len(W)):
        sum+=W[i]
        if sum<20:
            x=20-sum
        elif sum>20:
            x=sum-20
            while sum:
                if sum<20:
                    W[i]= W[i]+x
                elif sum>20:
                    W[i]=x-W[i+x]
        print(W[i])
