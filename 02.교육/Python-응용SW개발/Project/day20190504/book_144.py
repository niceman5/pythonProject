# 아톰에서 한글처리시 반드시 포함해야 한다.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 함수정의
#  매개변수 없고 리턴값 있음
def say():
    return 'Hi'

# 함수 호출
a = say()
print(a)


# 함수정의
# 매개변수 있고 리턴값 없음

def sum(a, b):
    print('%d, %d의 합은 %d입니다.'%(a, b, a+b))

c = sum(3,4)
print(c)
