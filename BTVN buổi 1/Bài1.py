x = int(input ("Nhap so x: " ))
y = int(input ("Nhap so y: " ))
print("tổng x + y = ", x + y)
print("hiệu x - y = ", x - y)
print("nhân x * y = ", x * y)
print("chia lấy nguyên x // y = ", x // y)
print("mũ x ** y = ", x ** y)
print("chia dư x % y = ", x % y)
# So sánh x và y:
if x > y:
    print("x lớn hơn y")
elif x < y:
    print ("x bé hơn y")
else:
    print ("x bằng y")
# x AND y
print("x AND y =", x & y)
# x OR y
print("x OR y =", x | y)
# x XOR y
print("x XOR y =", x ^ y)
# NOT x == y
print("NOT (x == y) =", not (x == y))
# x dịch phải 5 bit
print("x >> 5 =", x >> 5)
# x dịch  trái 6 bit
print("x << 6 =", x << 6)
# in hệ cơ số 2 đảo ngược của a
bin_x = bin(x)[2:]       
rev_bin_x = bin_x[::-1]  
print("Hệ nhị phân đảo ngược của x là:", rev_bin_x)