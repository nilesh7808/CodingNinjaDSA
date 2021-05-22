def stockSpan(price,n):
    i = 0
    while i != n:
        if price[i] == price[i+1]:
            return 1
        i = i + 1
        count = 0
        if price[i] < price[i+1]:
            count += 2
            i += 1
        elif price[i] > price[i+1]:
            count += 1
            i += 1

n = int(input())
price = [int(ele) for ele in input().split()]
spans = stockSpan(price,n)
for ele in price:
    print(ele,end= ' ')