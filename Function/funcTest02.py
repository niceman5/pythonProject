# 함수 클로져는 함수마다 독립적인 이름 공간을 제공
# 인스턴스객체처럼 별도로 작동하는 함수를 정의할수 있다.

def makeCount():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return  counter

# 프로그램 시작점
if __name__ == '__main__':
    c1 = makeCount()
    c2 = makeCount()

    print(c1())
    print(c2())
    print(c1())
    print(c1())
    print(c2())


