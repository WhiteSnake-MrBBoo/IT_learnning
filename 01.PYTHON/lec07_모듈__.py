# 함수에 return이 있으면 호출하는 쪽에서 변수에 담아 그 값을 사용
# 함수 정의
def add(a,b) :
    res = a + b
    return res

#----------------------------------------------------------

class PhoneBook :
    #생성자함수
    def __init__(self) :
        print("init함수 호출....")

    def addc(self,a,b) :
        res = a + b
        return res

    #----------------------------------------
    def loginc(name) :
        print(f"{name}님 로그인")

    def loginc22(self, name):
        print(f"{name}님 로그인")

    def loginc33(self, name):
        return name