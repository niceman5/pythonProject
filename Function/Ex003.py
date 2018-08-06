class Counter:
    def __init__(self, iValue = 0):
        self.cur = iValue
        self.step = 1
    def incr(self):
        self.cur += self.step

    # 출력하게 한다.
    def __repr__(self):
        return '{}'.format(self.cur)

    # 인스턴스를 직접호출하는 경우 실행되게 한다.
    def __call__(self):
        self.incr()
        return self.cur

# main 프로세스
if __name__ == '__main__':
    c = Counter()
    c.incr()
    c.incr()
    c.incr()
    print(c)
    c()     #  직접호출
    c()
    c()
    print(c)