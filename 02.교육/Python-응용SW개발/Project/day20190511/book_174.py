class Calculator:
    number = 10     # 클래스변수.
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result


# class의 인스턴스 생성안해도 사용가능
print(Calculator.number)

cal1 = Calculator()
cal2 = Calculator()
print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))
