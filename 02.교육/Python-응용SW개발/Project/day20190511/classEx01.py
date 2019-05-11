class Mother:
    money = 1000000    #class변수

    def buy(self):
        # class변수 사용시 해당 class명을 같이 써주어ㅓ야 한다.
        Mother.money -= 200000

    def balance(self):
        print('balance :', Mother.money)


# Mother를 상속한다.
class Son(Mother):
    def buy(self, money):
        Mother.money -= money


# 변수종류
# -전역변수
# -지역변수
# -class변수

s = Son()
s.buy(600000)
s.balance()

m = Mother()
m.buy()
m.balance()

print(issubclass(Son, Mother))  # 앞이 자식 뒤가 부목
print(issubclass(Mother, Son))

print(isinstance(s, Son))
print(isinstance(s, Mother))
