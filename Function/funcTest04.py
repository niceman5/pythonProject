

def frange(arg1, *args):

    if len(args) == 0:
        start , end , step = 0.0, float(arg1), 0.25
    elif len(args) == 1:
        start, end, step = float(arg1), float(args[0]), 0.25
    elif len(args) == 2:
        start, end, step = float(arg1), float(args[0]), float(args[1])
    L = []
    v = start
    if step > 0:
        while v < end:
            L.append( v )
            v += step
    elif step < 0:
        while v > end:
            L.append( v )
            v -= step

    return L


def mysum(*args):
    return sum(args)

# main 프로세스
if __name__ == '__main__':
    l = frange(1.0, 5.0, 0.3)
    print((l))
    # a = 1
    # assert(a in (0, 1))
    print(mysum())
    print(mysum(1, 2))
    print(mysum(1, 5 , 7, 2, 3))

    fnames = ['a_thumb.jpg', 'b01_thumb.jpg', 'S100_thumb.jpg', 'S100.jpg', 'b01.jpg']
    print(list(filter(lambda s: '_thumb' in s, fnames)))    # '_thumb'이 포함된 파일명만 리스트
    print(list(filter(lambda s: '_thumb' not in s, fnames)))    # '_thumb'이 포함안된 파일명만 리스트

    s = 'as soon as possible'
    # print(s.split(' '))
    # 단어를 나누고 단어의 첫 글자를 모아서 출력
    print(''.join(map(lambda s: s[0], s.split(' '))))

    # 파일을 읽어서 처리
    with open('aaa.txt', 'r') as f:
        L = list(map(lambda s: s.split(), f))

    # 파일을 읽어서 각 요소를 int로 만들어서 리스트로 다시 만듬
    with open('aaa.txt') as f:
        L = list(map(lambda s: list(map(int, s.split())), f))
    x, y, z = L
    print(x)    # 1 4 7
    print(y)    # 2 5 8
    print(z)    # 3 6 9

    x = list(map(lambda x: x[0], L))
    y = list(map(lambda x: x[1], L))
    z = list(map(lambda x: x[2], L))

    print(x)
    print(y)
    print(z)



