while True:
    day = int (input("Nhap ngay sinh: "))
    month = int (input("Nhap thang sinh: "))

    if(month == 3 and 21 <= day <=31) or (month == 4 and 1 <= day <= 19):
        print("Ban thuoc cung Bach Duong")
    elif(month == 4 and 20 <= day <=30) or (month == 5 and 1 <= day <= 20):
        print("Ban thuoc cung Kim Nguu")
    elif(month == 5 and 21 <= day <=31) or (month == 6 and 1 <= day <= 21):
        print("Ban thuoc cung Song Tu")
    elif(month == 6 and 22 <= day <=30) or (month == 7 and 1 <= day <= 22):
        print("Ban thuoc cung Cu Giai")
    elif(month == 7 and 23 <= day <=31) or (month == 8 and 1 <= day <= 22):
        print("Ban thuoc cung Su Tu")
    elif(month == 8 and 23 <= day <=31) or (month == 9 and 1 <= day <= 22):
        print("Ban thuoc cung Xu Nu")
    elif(month == 9 and 23 <= day <=30) or (month == 10 and 1 <= day <= 23):
        print("Ban thuoc cung Thien Binh")
    elif(month == 10 and 24 <= day <=31) or (month == 11 and 1 <= day <= 22):
        print("Ban thuoc cung Bo Cap")
    elif(month == 11 and 23 <= day <=30) or (month == 12 and 1 <= day <= 21):
        print("Ban thuoc cung Nhan Ma")
    elif(month == 12 and 22 <= day <=31) or (month == 1 and 1 <= day <= 19):
        print("Ban thuoc cung Ma Ket")
    elif(month == 1 and 20 <= day <=31) or (month == 2 and 1 <= day <= 18):
        print("Ban thuoc cung Bao Binh")
    elif(month == 2 and 19 <= day <=29) or (month == 3 and 1 <= day <= 20):
        print("Ban thuoc cung Song Ngu")
    else:
        print("Ngay thang khong hop le. Vui long nhap lai.")

    tiep_tuc = input("Ban co muon tiep tuc k ? ")
    if tiep_tuc == 'n' or tiep_tuc == 'N':
        print ("Chuong trinh ket thuc!")
        break