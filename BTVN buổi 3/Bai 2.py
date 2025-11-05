chuoi = input("Nhập chuỗi từ bàn phím: ")

# 1. Loại bỏ ký tự không phải chữ hoặc khoảng trắng
chuoi1 = []
for ch in chuoi:
    if ch.isalpha() or ch.isspace():
        chuoi1.append(ch)

# 2. Chuyển về chữ thường
chuoi1 = ''.join(chuoi1).lower()

# 3. Đếm nguyên âm và phụ âm
nguyen_am = ['a', 'e', 'i', 'o', 'u']
dem_nguyen_am = 0
dem_phu_am = 0
for ch in chuoi1:
    if ch.isalpha():
        if ch in nguyen_am:
            dem_nguyen_am += 1
        else:
            dem_phu_am += 1

# 4. Tách chuỗi thành danh sách từ rồi đảo ngược từng từ
chuoi_moi = chuoi1.split()
chuoi_dao_nguoc = [tu[::-1] for tu in chuoi_moi]

# 5. Kiểm tra chuỗi có phải palindrome (bỏ qua khoảng trắng)
kiem_tra = chuoi1.replace(" ", "")
palindrome = kiem_tra == kiem_tra[::-1]

# 6. In kết quả
print("Chuỗi sau khi làm sạch:", chuoi1)
print("Số lượng nguyên âm:", dem_nguyen_am)
print("Số lượng phụ âm:", dem_phu_am)
print("Chuỗi sau khi đảo ngược từng từ:", ' '.join(chuoi_dao_nguoc))
if palindrome:
    print("Chuỗi là palindrome")
else:
    print("Chuỗi không phải palindrome")
