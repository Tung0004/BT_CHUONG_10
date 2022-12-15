a=int(input("nhập a: "))
b=int(input("nhập b: "))
c=int(input("nhập c: "))
import math
delta=math.pow(b,2)-4*a*c
if a==0 and b==0:
    print("pt vô nghiệm")
elif a==0 and b!=0:
    print("pt có nghiệm",-c/b)
elif delta>0:
    print("pt có 2 nghiệm phân biệt :",)

