print("Chao mung den CLB Tin Hoc HIT")
print('CLB Tin Hoc HIT truc thuoc Truong CNTT  - "10 diem"')
s = "CLB Tin Hoc HIT truc thuoc Truong CNTT "
print("Các chữ cái in hoa:", ''.join([c for c in s if c.isupper()]))

print("Các chữ cái thường:", ''.join([c for c in s if c.islower()]))

if "CNTT" in s:
    print("Yes")
else:
    print("No")

print("Chuỗi sau khi đổi hoa <-> thường:", s.swapcase())
