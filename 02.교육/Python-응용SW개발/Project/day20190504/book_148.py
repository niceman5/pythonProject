# 아톰에서 한글처리시 반드시 포함해야 한다.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


def sum_mul(choice, *args):
    print('choice :', choice)
    if choice == 'sum' :
        result = 0
        for n in args:
            result = result + n
    elif choice == 'mul':
        result = 1
        for n in args:
            result = result * n
    return result


result = sum_mul('sum', 1,2,3,4,5)
print('1-5누적합 : ', result)
result = sum_mul('mul', 1,2,3,4,5)
print('1-5누적곱 : ', result)
