def sumNaturals(n):

    #base case
    if n == 1:
        return 1

    #induction hypothesis and induction
    smallOutput = sumNaturals(n-1) + n
    return smallOutput

n = int(input())
print(sumNaturals(n))