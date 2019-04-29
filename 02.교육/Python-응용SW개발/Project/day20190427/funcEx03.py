# 아톰에서 한글처리시 반드시 포함해야 한다.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 기본값 설정
# 인수의 기본 값
def default_func(arg=1):
    print('arg=',arg)

# 리턴값
# 기능 " 인수의 2배리턴
def mul(num):
    num *= 2
    return num

#dvi 함수를 정의하고 호츌
# 인수 2개를 받아서 몫계산해서 리턴
def div(a, b):
    if b == 0:
        return 0, 0
    return a // b, a% b     # 튜플로 리턴한다.
# default_func(100)
# default_func()
#
# result = mul(100)
# print('result=', result)


re = div(10, 3)
print(re, type(re))
print(re[0], re[1])
print(div(10, 0))
