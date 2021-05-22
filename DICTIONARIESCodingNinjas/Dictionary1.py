a = { 1:2, 3:4, "list":[1 , 2, 3, 4 ], "dict":{3:6} }
print(a)

print(a['list'])

print(a['dict'])

print(a.get('list'))

print(a.get('li'))

print(a.get('li','Not Present'))

print(a.keys())

print(a.values())

print(a.items())

for i in a:
    print(i,a[i])

for i in a.values():
    print(i)

print("list" in a)

a['t'] = (8, 9, 10)

print(a)

print(a[1])
a[1] = 10
print(a[1])

b = {3:5, "apple": "fruit"}
a.update(b)
print(a)