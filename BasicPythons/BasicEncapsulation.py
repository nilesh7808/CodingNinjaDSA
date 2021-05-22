class A:
    def __init__(self):
        self._name="Nilesh"

class B(A):
    def __init__(self):
        print("Derived class has been called")

        A.__init__(self)
        print("Calling Protected member from the base class(A)")
        print(self._name)

o = B()
o1 = A()
print(o._name)
print(o1._name)