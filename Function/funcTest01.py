# 함수에 list를 전달하면 함수내에서 값을 변경할수 있음.
# 이것도 리스트내의 값을 직접 변경하면 되지만 리스트자체를 할당하면 안됨
# 튜플이나 일반적인 값은 변경안됨

# 파이썬에서 변수를 찾는 규칙
# L : local, 함수내에서 선언된 지역 변수
# E : Enclosing Function Local 함수를 내포하는 또 다른 함수 영역
# G : Global 함수 영역에 포함되지 않은 모듈 영역
# B : Bulit-in 내장영역

# global 선언자 : 함수를 전역변수임을 선언

# 가변인수 리스트
# def vargs(a, *arg):
#     print(a, arg)
# --> arg는 튜플로 받는다.

# 정의되지 않은 인수 처리하기
# def f(width, height, **kw)
# --> **kw는 리스트로 받게 된다. 이때는 반드시 key, value를 맞춰서 받아야 한다.


class MyClass:
    # 해당 클래스에서 +를 선언
    # + 연산을 수행하면 각 객체의 __add__메서드를 호출한다.
    # 함수에서 반환값이 없으면 None가 반환됨
    def __add__(self, b):
        print('add %s is called' % b)


# 프로그램 시작점
if __name__ == '__main__':
    c = MyClass()
    print(c + 1)
    print(c + 'abc')