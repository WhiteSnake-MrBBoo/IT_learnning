from lec_python.lec07_모듈__ import add
son = add(4, 5)
print("받았음", son)

from lec07_모듈__ import add
son = add(4, 5)
print("받았음", son)

import lec07_모듈__
son = lec07_모듈__.add(4,5)
print("받았음", son)

import lec07_모듈__ as aa
son = aa.add(4,5)
print("받았음", son)

#----------------------------------------------------------
from  lec07_모듈__ import PhoneBook

pb = PhoneBook()
#print(pb)

a = pb.addc(5,3)
print(a)


#----------------------------------------
PhoneBook.loginc("홍길동")

pb.loginc22("홍길동")

a = pb.loginc33("홍길동")
print(f"{a}님 로그인")
