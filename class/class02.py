
class MyStr:
    def __init__(self, s):
        self.s = s
    def __add__(self, s):
        return MyStr(self.s + str(s))

    def __sub__(self, o):
        try:
            k = self.s.index(o)
            return MyStr(self.s[:k] + self.s[k + len(o):])
        except ValueError:
            return self
    def __repr__(self):
        return 'MyStr('+ self.s +')'
    def __str__(self):
        return 'MyStr(' + self.s + ')'

# main 프로세스
if __name__ == '__main__':
    a = MyStr("I like python and python")
    print(a)
    print(a + ' stuff')
    print(a - ' python')


