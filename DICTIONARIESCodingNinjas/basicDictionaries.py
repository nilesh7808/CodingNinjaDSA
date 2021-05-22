a = { }
print(type(a))

a = { 1: "Mommy", 2: "Papa", 3: "Bhaiya", 4: "Nilesh", 5: "Ruchi" }
print(len(a))
print(a)

b = a.copy()
print(b)

c = dict([(1, "Nilesh"), (2,"Ruchi"), (3, "Raj")])
print(c)

d = dict.fromkeys([1, 2, 3])
print(d)

d = dict.fromkeys([1, 2, 3], 10)
print(d)

e = dict.fromkeys([(1,2),(2,3)])
print(e)
