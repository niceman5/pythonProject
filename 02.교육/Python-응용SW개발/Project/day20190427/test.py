# 아톰에서 한글처리시 반드시 포함해야 한다.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 함수정의
# def 함수명(변수명):
#     명령문
#     return 값
def sum(a : int, b : int) -> int:
    s = a + b
    print(s)
    return s

def hello():
    print('hello~~~~')

def apple_count(apple):
    print('사과', apple)

aaa = sum(10,10)
print(aaa)

print( sum(2.1, 3.5))
print( sum('good', 'day'))

# print( sum(10))   # 에러
hello()
apple_count('가나다')
