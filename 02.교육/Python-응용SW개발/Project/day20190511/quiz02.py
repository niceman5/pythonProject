# 아톰에서 한글처리시 반드시 포함해야 한다.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

list_value = ['100', 'good', '5', '250', 'hi', '500']
list_number = []

for v in list_value:
    try:
        n = int(v)
        list_number.append(v)
    except:
        continue

print('list_value에서 숫자만 출력:', list_number)
