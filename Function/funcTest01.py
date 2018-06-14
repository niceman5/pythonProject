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