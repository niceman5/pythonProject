# 한줄 짜리 람다함수
# g = lambda x, y: x * y
#            함수인수 : 반환될 값
# return문이 없어도 하나의 식을 이루는 값을 반환 한다.



def f(x):
    return x * x

if __name__ == '__main__':
    g = lambda x, y: x * y
    print(g(12, 2))

    # map 함수
    # map함수에서 첫번째 인수는 함수 f이고 두번째인수는 리스트 X임
    # 두번째인수의 모든 항목은 첫 인수인 함수 f에 적용되고 결과로 반복자인 map객체를 반환한다.
    X = [1, 2, 3, 4, 5]

    # print(map(f, X))
    l = list(map(f, X))
    print(l)

    # map함수는 필요한 시점에 계산이 이루어지는 반복자....
    # next()를 통해서 다음 연산 실행할수 있음.
    # map함수에 람다함수를 사용할수 있다.
    m = map(f, X)
    print(next(m))
    print(next(m))
    print(next(m))
    print(next(m))
    print(next(m))

    X = range(10)
    Y = map(lambda x: x * x + 4, X)
    l = list(Y)
    print(l)

    # map함수는 입력을 두개 이상도 받는다.
    X = [1, 2, 3, 4, 5]
    Y = [6, 7, 8, 9, 10]

    Z = map(lambda x, y:x + y, X, Y)
    print(list(Z))

    # filter
    # 필터링하여 참인 요소만 출력. 첫번째 인수는 함수고 두번째는 시퀀스 자료형
    f = filter(lambda x: x > 2, [1, 2, 3, 4, 5])
    print(list(f))

    # 함수 객체의 속성
    def f(a, b, c = 1):
        '함수의 속성값을 설명합니다.'
        return a

    print(f.__doc__)
    print(f.__name__)




