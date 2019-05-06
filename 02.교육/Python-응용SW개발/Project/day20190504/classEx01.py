
# class정의
# 인스턴스 변수는 self가 붙음

class Student():
    nick = 'google'  # class변수 class로 만든 객체가 공유해서 사용한다.

    def study(self):
        print('study~~~~!!!')
        print('nick=', Student.nick)    #class변수라서 class명을 쓴다.
        print('name=', self.name)

    def setName(self, name):
        print('nick=', Student.nick)
        self.name = name                # 인스턴스  변수가 생성됨

s = Student()
s1 = Student()
# # s.setName('Kim')
# # s.study()
# # print(s.name)

#
# s.setName('Park')
# s1.setName('Hong')
#
# s.study()
# s1.study()

# print(Student.nick)     # class 인스턴스안 만들고 사용가능
# print(self.name)
