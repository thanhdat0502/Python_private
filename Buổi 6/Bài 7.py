from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def dientich(selt):
        pass
    @abstractmethod
    def chuvi(self):
        pass
    def inTT(self):
        print ("Dien tich:", self.dientich())
        print ("Chu vi:", self.chuvi())

class hinhchunhat(shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def dientich(self):
        return self.width * self.height
    def chuvi(self):
        return 2* (self.width + self.height)
     
h1 =hinhchunhat(3,4)
h1.inTT()