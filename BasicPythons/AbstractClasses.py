from abc import ABC, abstractmethod
class Automobile(ABC):
    def __init__(self):
        print("Automobile has been created")

    @abstractmethod
    def start(self):
        print("Start of Automobile has been called")

    @abstractmethod
    def stop(self):
        pass

class Car(Automobile):
    def start(self):
        # super(Car, self).start()
        print("Start of Car has been called")

    def stop(self):
        pass

c = Car()
c.start()