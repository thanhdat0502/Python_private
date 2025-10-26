tong_tien = 0
so_mon = 0
while True:
    ten_mon = input("Nhap ten mon: ")
    if ten_mon== "x" or ten_mon == "X":  
        break
    elif ten_mon == "skip": 
        continue
    elif ten_mon== "pass":  
        pass
        continue

    gia = input("Nhap gia tien: ")
    hop_le = True
    for a in gia:
        if a not in "0123456789":
            hop_le = False
            break

    if hop_le:
        tong_tien += int(gia)
        so_mon += 1
    else:
        print("Gia tien khong hop le! Bo qua mon nay.")

print("so mon:", so_mon)
print("Tong tien truoc khi giam: ",tong_tien)

if tong_tien > 200000:
    giam = tong_tien * 0.1
    tong_tien -= giam
    print("So tien giam: ", giam)
else:
    giam = 0
    print ("Khong duoc giam gia.")

print("Tong tien phai tra: ", tong_tien)
