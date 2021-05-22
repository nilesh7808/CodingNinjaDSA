def powerNumber(a,b):
    #base case

    if b == 0:
        return 1
    #induction hypothesis and induction process
    # if b is even
    if b % 2 == 0:
        return powerNumber(a**2,b//2)

    #if b is odd
    return a * powerNumber(a, b-1)

a = int(input())
b = int(input())
print(powerNumber(a,b))
