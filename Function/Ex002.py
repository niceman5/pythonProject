
class Square:
    def __init__(self, cnt):
        self.cnt = cnt

    def __getitem__(self, k):
        if 0 <= k <= self.cnt:
            return k*k
        raise IndexError('out of range {}'.format(k))

# main 프로세스
if __name__ == '__main__':
    s = Square(10)
    print(s[2])
    print(s[9])
    print(list(s))
    for ele in s:
        print(ele, end=' ')

    print(s[10])
    # print(s[11])  index오류를 낸다.