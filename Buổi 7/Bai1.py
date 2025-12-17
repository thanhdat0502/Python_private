class Book:
    def __init__ (self,id,title,author,year):
        self.id =id
        self.title = title
        self.author = author 
        self.year = year
        self.status = "available"
class Library:
    def __init__(self):
        self.book = []
    def add_book(self,book):
        self.book.append(book)
        print("Đã thêm sách!")
    def remove_book(self,book,id):
        for b in book:
            if b.id == id:
                book.remove(b)
                return "Đẫ xóa sách thành công!"
        return "Không tìm thấy sách!"
    def tim__kiem(self,book,title):
        for b in book:
            if b.title == title:
                return b
        return "Không tìm thấy sách!"
    def muon_sach(self,book,id):
        for b in book:
            if b.id == id:
                if b.status == "borrowed":
                    return "Sách đã được mượn!"
                b.status = "borrowed"
                return "Đã mượn sách thành công!"
        return "Không tìm thấy sách!"
    def tra_sach(self,book,id):
        for b in book:
            if b.id == id:
                if b.status == "available":
                    return "Sách chưa đc mượn!"
                b.status == "available"
                return "Sách tra thành công!"

    def show_book(self):
            for b in self.book:
                print(b.id, b.title, b.author, b.year, b.status)

Lib = Library()
b1 = Book(1,"doraemon","truyen dài", 2025)
b2 = Book(2,"naruto",'truyeenj ngan',2018)

Lib.add_book(b1)
Lib.add_book(b2)    
Lib.show_book()