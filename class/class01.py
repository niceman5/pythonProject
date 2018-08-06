# 클래스는 연산자 중복을 지원한다. 파이썬에서 사용하는 모든 연산자의 동작을 정의할수 있다.
class MyClass:

    # 객체가 생성되고 나서 자동으로 실행된다.
    def __init__(self):
        self.value = 0
    
    # 기본연산자를 재정의한다.
    def __add__(self, x):
        print('add {} call'.format(x))
        return x
    # 소멸자. 객체가 삭제될때 실행된다.....  del로 객체 삭제시...
    def __del__(self):
        print('소멸자')

# main 프로세스
if __name__ == '__main__':
    a = MyClass()
    print(a.value)
    b = a + 3

    print(b)
