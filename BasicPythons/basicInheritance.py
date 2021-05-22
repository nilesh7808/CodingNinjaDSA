class Vehicle:
    def __init__(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setColor(self, color):
        return self.__color

class Car(Vehicle):
    def printCar(self):
        print("Car is:",self.getColor())

c = Car("Red")
c.printCar()