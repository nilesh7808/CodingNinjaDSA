def greatest_In_Tuple():
    print(max(t))
print("Enter numbers seperated by comma ")
t = tuple(list(int(i) for i in input().split(",")))
greatest_In_Tuple()
