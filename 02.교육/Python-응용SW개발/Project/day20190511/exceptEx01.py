# try:
#     # 예외가발생
#
# except:
#     # 예외가발생했을때 처리할 명령
#
# else:
#     #예외가 발생하지 않았을 때
# finally:
#     #예외 발생 여부와 상관없이 무조건 마지막에 실행하고자하는 명령문.
#

n1 = 5
n2 = 0

result1, result2 = 0, 0

try:
    result1 = n1 / n2
    result2 = n1 % n2
except:
    print('exception')
else:
    print('n1 / n2 :', result1)
    print('n1 % n2 :', result2)
finally:
    print('exception end!!!')

print('success~!!')
