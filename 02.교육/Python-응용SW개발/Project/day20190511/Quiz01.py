# 아톰에서 한글처리시 반드시 포함해야 한다.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# class Annimal:
#     def __init__(self):
#         pass
#
#     def print_name(self, name):
#         name = name
#
#
# class Dog(Annimal):
#     def __init__(self, name):
#         self.name = name
#
#     def sounds(self):
#         print('이름은 {} 입니다.'.format(self.name))
#
# class Cat(Annimal):
#     def __init__(self, name):
#         pass
#
#     def sounds(self):
#         print

class Annimal:
    def __init__(self, name):
        self.name = name    #인스턴스 변수 name에 설정

    def print_name(self):
        print('이름은 {} 입니다.'.format(self.name))

# Annimal을 상속받는다.
# Dog에는 생성자가 없음으로 Annimal의 생성자를 사용한다.
# 해당 method를 찾아서 실행하고 없으면 부모클래스의 함수를 찾아서 실행한다.
class Dog(Annimal):
    def sounds(self):
        print(self.name + '가 멍멍 짖어요.')

    def testPrint(self):
        print('run testPrint()')


class Cat(Annimal):
    def __init__(self, name):
        super().__init__(name)  #부모의 생성자를 실행. self외 매개변수 넣어야 함.
        print('Cat__init__')
        self.sounds()

    def sounds(self):
        print(self.name + '가 야옹 울어요.')

#[방법1] 객체 생성없이 클래스함수 호출
Dog.testPrint(Dog('happy'))

# [방법2] 객체 생성후 클래스 함수 호출
d = Dog('happy')
Dog.testPrint(d)

# d = Dog('happy')
# c = Cat('world')
#
# d.print_name()
# d.sounds()
#
# c.print_name()
# c.sounds()
