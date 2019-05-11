# 아톰에서 한글처리시 반드시 포함해야 한다.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class Service:
    secret = '영구는 배꼼이 두개'
    # 생성자는 객체 생성시 자동으로 호출
    # 생성자는 함수
    # 객체 생성시 변수의 값을 설정하거나 특정한 함수를 실행하고 싶을때
    def __init__(self, name):
        self.name = name

    def setname(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print('%s님 %s + %s = %s 입니다.'%(self.name, a, b, result))



pey = Service('강강강')
print(pey.secret)
print(Service.secret)
# pey.setname('홍길동')
pey.sum(1,1)

# pey.sum(pey, 1, 1)    안됨
Service.sum(pey, 1, 1)  #객체를 반드시 넣어줘야 함.
