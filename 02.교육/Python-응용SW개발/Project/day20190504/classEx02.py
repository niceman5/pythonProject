
class Person():
    def setName(self, name):
        nick = 'aa'         # 지역변수..해당 함수내에서만 사용한다.
        self.name = name

    def setAge(self, age):
        self.age = age

    def info(self):
        print('name : {}, age : {}'.format(self.name, self.age))

p = Person()
p.setName('kim')    # 인스턴스 변수 여기서 만들어지기 때문에 이거 호출안하면 못 씀
p.setAge(25)
p.info()
