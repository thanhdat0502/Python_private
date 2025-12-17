class student:
    def __init__(self,name,age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def describe(self):
        print(f"ten hoc sinh: {self.name}")
        print(f"tuoi hoc sinh: {self.age}")
        print(f"truong hoc sinh: {self.grade}")

class teacher:
    def __init__(self, name, age,subject):
        self.name = name
        self.age = age
        self.subject = subject
    def describe(self):
        print(f"ten giao vien: {self.name}")
        print(f"tuoi giao vien: {self.age}")
        print(f"du an giao vien: {self.subject}")

class doctor:
    def __init__(self, name, age, specialist):
        self.name = name
        self.age = age
        self.specialist = specialist
    def describe(self):
        print(f"ten bac si: {self.name}")
        print(f"tuoi bac si: {self.age}")
        print(f"chuyen nganh bac si: {self.specialist}")

class Ward:
    def __init__(self, name):
        self.name = name
        self.listPerson = []
    def addPerson(self, person):
        self.listPerson.append(person)
    def describe(self):
        print(f"ten phong: {self.name}")
        for i in self.listPerson:
            i.describe()
            print("------------------")
    def countDoctor(self):
        count = 0
        for i in self.listPerson:
            if isinstance(i, doctor):
                count += 1
        return count
    def sortAge(self):
        self.listPerson.sort(key = lambda x: x.age)

student1 = student("Mai Van Thanh Dat", 19, "sinh vien")
teacher1 = teacher("Le Dinh Van ", 36, "Giao vien Hoa")
doctor1 = doctor("Mai Thi Mai Phuong", 32, "Tai mui hong")
teacher2 = teacher(" nguyen Doan Dung", 35, "Giao vien Ly")
doctor2 = doctor("Nguyen manh Trương" , 32, "gây mê")

Ward1 = Ward("Phong 1")
Ward1.addPerson(student1)
Ward1.addPerson(teacher1)
Ward1.addPerson(doctor1)
Ward1.addPerson(teacher2)
Ward1.addPerson(doctor2)

Ward1.describe()

print(f"so luong bac si: {Ward1.countDoctor()}")
print(f"-----sap xep theo tuoi:--------")
Ward1.sortAge()
print(Ward1.describe())