class Smartphon:
    def __init__(self, name ,color):
        self.name = name
        self.color =color
    def Inthongtin(self):
        print("Ten iphone:",self.name)  
        print ("Mau iphone:", self.color)
Newphone = Smartphon("Iphone 17", "Mau đỏ")
Newphone.Inthongtin()

