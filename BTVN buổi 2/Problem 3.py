print ("Nhap so sinh vien: ")
n = int(input())
for i in range (n):
    print ("Nhap thong tin sinh vien thư ",i+1)
    hoten = input("Ho va ten: ")
    diem1 =int(input("Diem lan 1:"))
    diem2 =int(input("Diem lan 2:"))

    tong = diem1 + diem2
    if tong >= 200:
        xeploai ="Xuat sac"
    elif tong >= 150:
        xeploai ="Gioi"
    elif tong >= 100:
        xeploai ="Kha"
    else:
        xeploai ="Yeu"

    print ("Ho va ten:" , hoten)
    print ("Diem tong" , tong)
    print ("Xep loai:", xeploai)
