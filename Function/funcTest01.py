# 함수에 list를 전달하면 함수내에서 값을 변경할수 있음.
# 이것도 리스트내의 값을 직접 변경하면 되지만 리스트자체를 할당하면 안됨
# 튜플이나 일반적인 값은 변경안됨


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