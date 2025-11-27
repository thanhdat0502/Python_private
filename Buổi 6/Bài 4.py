class Animal:
    def __init__(self, trong_luong, chieu_cao):
        self.trong_luong = trong_luong
        self.chieu_cao = chieu_cao
    def thongtin(self):
        print("Trong luong:", self.trong_luong)
        print("Chieu cao:", self.chieu_cao)

class con_meo(Animal):
    def __init__(self, trong_luong, chieu_cao, mau_long):
        super() .__init__(trong_luong,chieu_cao)
        self.mau_long = mau_long
    
    def thongtin(self):
        super() .thongtin()
        print("Mau long cua meo:", self.mau_long)

x = con_meo(3, 30, "den")
x.thongtin()