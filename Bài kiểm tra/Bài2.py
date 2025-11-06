chuoi = input ("Nhap chuoi: ")
chuoi = chuoi.lower()
dem_chu = {}
for ch in chuoi:
    if ch.isalpha():
        if ch in dem_chu:
            dem_chu[ch] += 1
        else:
            dem_chu[ch] = 1
print ("So lan xuat hien cua moi ky tu chu trong chuoi:")
for ch, dem in dem_chu.items():
    print (f"'{ch}': {dem}")
