class Cal:
    def setdata(self, first, second):
        self.first = first
        self.second =  second

    def sum(self):
        result = self.first +  self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


# 객체 인스턴스 생성
a = Cal()
a.setdata(4,2)
print(type(a))
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())
