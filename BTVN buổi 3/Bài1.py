numbers = list(map(int, input("nhap cac so nguyen tu ban phim: ").split()))
# 1. in danh sach sau khi soat trung lap
number1 =[]
for n in numbers:
    if n not in number1:
        number1 .append(n)
print("danh sach sau khi loai bo cac so trung la: ", number1)
#2. danh sach sau khi bien doi
number2 =[]
for n in number1:
    if n % 2 == 0:
        number2 .append(n**2)
    else:
        number2 .append(n**3)
print("danh sach sau khi bien doi la: ", number2)

#3.