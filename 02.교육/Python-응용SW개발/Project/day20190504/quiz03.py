class Dog():
    # 생성자를 별도로 안만들면 자동으로 아래 생성자가 추가된다.
    # def __init__(self):
    #     pass

    def __init__(self, name):
        self.name = name

    def showName(self):
        print(self.name)


d = Dog('aaaa')
d.showName()
