class person:
    def __init__ (self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        if len (name) > 0:
            self.__name = name
        else:
            print("Ten khong hop le!")


    # def introduce(self):
    #     print("Hello, my name is:", self.name)

x = person("Mai Van Thanh Dat",19)
# x.introduce()
print(x.get_name())

x.set_name("Dang")
print(x.get_name())