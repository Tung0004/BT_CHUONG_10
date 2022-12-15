#sử dụng hàm pow
import math
x=int(input("nhập x:"))
n=int(input("nhập n:"))
def tinh_S(x,n):
    S=math.pow(math.pow(x,2)+1,n)
    return S

print("S = ",tinh_S(x,n))
