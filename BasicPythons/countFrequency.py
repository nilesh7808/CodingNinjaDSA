def count_Frequency():
    i = 0
    for ele in t:
        if i == t.index(ele):
            print(ele,"->",t.count(ele))
        i += 1
print("Enter The Numbers ")
t = tuple([int(ele) for ele in input().split(",")])
count_Frequency()
