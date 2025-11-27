class Smartphone:
    Price = 1000000000
    # định nghĩa phương thức khởi tạo
    def __init__ (self, name):
        #Bien thể hiện thường đc khai báo trong hàm init:
        self.name = name
    
    def inthongtin(self, color = None):
        if color is not  None:
            self.color =color
        #Biến thể hiện khai báo trong hàm khác:
        print("Ten iphone:",self.name )
        print("Mau cua iphone:",self.color)
        print("Giá:", Smartphone.Price)

Newphone = Smartphone("Iphone 16")
Oldphone = Smartphone("Samsung")
Newphone.inthongtin("titan")
Oldphone.inthongtin("Den")





