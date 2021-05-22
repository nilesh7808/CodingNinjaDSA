class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return (self.a + other.a, self.b + other.b)


A = Add(1,2)
B = Add(3,4)
print(A+B)