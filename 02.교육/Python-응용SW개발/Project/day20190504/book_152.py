# 아톰에서 한글처리시 반드시 포함해야 한다.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



def say_myself(name, old, man=True):
    print('나의 이름은 %s입니다.'%(name))
    print('나이는 %d입니다.'%(old))
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself('홍길동', 30)

# 위치가 틀려도 매개변수가 맞으면 됨
say_myself(man=False, name='이미자', old=35)
