
class Person():
    # 생성자
    # 객체생성시 자동으로 호출
    # 1)인스턴스 변수의 값을 자동으로 초기화하고자 할때
    # 2)객체 생성시 자동으로 함수를 실행하고 싶을때
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.test()     # 함수 호출도 가능함.

    def setName(self, name):
        nick = 'aa'         # 지역변수..해당 함수내에서만 사용한다.
        self.name = name

    def setAge(self, age):
        self.age = age

    def info(self):
        print('name : {}, age : {}'.format(self.name, self.age))

    def test(self):
        print('test')

p = Person('jang', 25)
p.info()
p.test()
