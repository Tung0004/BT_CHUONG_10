import time
from datetime import datetime
ngay=int(input("nhập ngày: "))
thang=int(input("nhập tháng: "))
nam=int(input("nhập tháng: "))
ngay_thang_nam=datetime(nam,thang,ngay)
import calendar
print("ngày tháng năm vừa nhập: ",ngay_thang_nam.strftime("%d-%m-%Y"))
if calendar.isleap(nam) is True:
    print("năm",nam,"là năm nhuận")
else:
    print("năm",nam,"là năm không nhuận")
if calendar.weekday(nam,thang,ngay) ==0:    
   print(ngay_thang_nam.strftime("%d-%m-%Y"),"là thứ 2")
elif calendar.weekday(nam,thang,ngay) ==1:
    print(ngay_thang_nam.strftime("%d-%m-%Y"),"là thứ 3")
elif calendar.weekday(nam,thang,ngay) ==2:
    print(ngay_thang_nam.strftime("%d-%m-%Y"),"là thứ 4")
elif calendar.weekday(nam,thang,ngay) ==3:
    print(ngay_thang_nam.strftime("%d-%m-%Y"),"là thứ 5")
elif calendar.weekday(nam,thang,ngay) ==4:
    print(ngay_thang_nam.strftime("%d-%m-%Y"),"là thứ 6")
elif calendar.weekday(nam,thang,ngay) ==5:
    print(ngay_thang_nam.strftime("%d-%m-%Y"),"là thứ 7")
elif calendar.weekday(nam,thang,ngay) ==6:
    print(ngay_thang_nam.strftime("%d-%m-%Y"),"là chủ nhật")
else :print("ngày",ngay,"không hợp lệ")

if thang in (1,3,5,7,8,10,12):
    print("tháng",thang,"có 31 ngày")
elif thang in(4,6,9,11):
    print("tháng",thang,"có 30 ngày")
elif calendar.isleap(nam) is True and thang==2:
    print("tháng",thang,"có 29 ngày")
elif calendar.isleap(nam) is False and thang==2:
    print("tháng",thang,"có 28 ngày")
else:
    print("tháng",thang,"không hợp lệ")