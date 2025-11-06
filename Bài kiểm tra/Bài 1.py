chuoi = "TV, Laptop, Phone, TV, Tablet, Laptop, Camera"

list1 = chuoi.split(", ")
print("Chuyển chuỗi thành list:", list1)

list2 = set(list1)
print("Loại bỏ trùng lặp bằng set:", list2)

list3 = tuple(list2)
print("Chuyển set thành tuple:", list3)

so_hang = len(list3) 
print("Số loại hàng hóa là:", so_hang)

kho_hang = {"Phone", "Laptop", "Smartwatch"}

co_va_banchay = list2.intersection(kho_hang)
print("Sản phẩm vừa có trong kho vừa bán chạy:", co_va_banchay)

chi_co_trong_kho = list2.difference(kho_hang)
print("Sản phẩm chỉ có trong kho nhưng không bán chạy:", chi_co_trong_kho)
