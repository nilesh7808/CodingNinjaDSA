def BinaryToDecimal(i):
    pass

def decimalToBinary(N):
    if N > 1:
        decimalToBinary(N // 2)
    x = str(N % 2)
    x = list(x)
    print(x)
    # for i in range(0,len(x)):
    #     if i == 0:
    #         i = 1
    #     d = int(i,2)
    # a =

N = int(input())
decimalToBinary(N)
