#sử dụng hàm pow
import math
x=int(input("nhập giá trị x:"))
n=int(input("nhập giá trị n:"))
def tinh_A(x,n):
    A=math.pow(math.pow(x,2)+x+1,n)+math.pow(math.pow(x,2)-x+1,n)
    return A
print("A= ",tinh_A(x,n))
