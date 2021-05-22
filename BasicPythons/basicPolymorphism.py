class Vehicle:
    def __init__(self, color):
        self.color = color

    def print(self):
        print("Color is:",self.color)

class Car(Vehicle):
    def print(self):
        # super().print()
        print("This is awesome")

c = Car("Black")
c.print()
