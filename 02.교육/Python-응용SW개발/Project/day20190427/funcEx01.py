def sum(a, b, *args):
    result = a +  b
    print('result=',result)

    for i in args:
        print(i)

# def aaa2( *args):     단독은 안됨
def sum2(a, *args):     # 필수로 받고 인수식으로 받는다. args는 튜풀이라 편짐안됨
    print(type(args))
    result = 0
    args = list(args)   # tuple을 list로 변경해서 인수 조정
    args.append(10)
    for i in args:
        result += i

    print('result2=', result+a)



sum(3,4,5,6,7)
sum(3,4)

sum2(3,4,5,7)
sum2(3,4)
