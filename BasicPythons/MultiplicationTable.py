def Table_Of_A_Number(N):

    for i in range(1, 11):
        x = N * i
        print("{}".format(N*i),"=",x, end=" ")

N = int(input("Enter a Number: "))
Table_Of_A_Number(N)