class Smartphone:

    @staticmethod
    def _trongluong(weight):
        print("Trong luong cua iphone:", weight)
Smartphone._trongluong(100)
newphone = Smartphone()
newphone._trongluong(10)

print("---------------------------------------------------------------------------------------------------------------------------------------------")

class hinhtron:
    def __init__(self, bankinh):
        self.bankinh = bankinh
    def chuvi(self):
        return self.bankinh * 2 * 3.14
    def dientich(self):
        return self.bankinh ** 2 *3.14

h1 = hinhtron(3)
print("Chu vi hinh tron:", h1.chuvi())
print("Dien tich hinh tron:", h1.dientich())