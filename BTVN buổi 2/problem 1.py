def giaiThua(n):
    if n ==0 or n ==1:
        return 1;
    gt =1
    for i in range (2, n+1):
        gt *= i
    return gt

# tinh e^x:
def tinhE_x(x, n):
    e_x=1
    for i in range (1, n+1):
        e_x += (x**i) / giaiThua(i)
    return e_x
    
# tinh S:
def tinhS(x,n):
    S= 1 
    for i in range (2, n+1):
        S+= 1/giaiThua(i)
    return S
    
x = float(input("Nhap x: "))    
n = int(input("Nhap n: "))
print ("e^x = ", tinhE_x(x,n))
print ("S = ", tinhS(x,n))