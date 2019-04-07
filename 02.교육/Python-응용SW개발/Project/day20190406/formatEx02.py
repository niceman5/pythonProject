## 정수
num1 = 25
print('[%d]'%(num1))     #왼쪽 정렬
print('[%5d]'%(num1))    #자리수가 정해지면 오른쪽 정렬
print('[%-5d]'%(num1))   #왼쪽정렬옵션

print('%-5d|'%(num1))   #왼쪽정렬옵션
print('%+5d|'%(num1))   #양수기호가 표시됨

print('[%05d]'%(num1))    #전체는 5자리 데이터가 빈자리는 0으로
print('%d, %o, %x'%(num1,num1,num1))

print('%d, %#o, %#x'%(num1,num1,num1))


# 실수
num2 = 2.345
print('%f'%(num2))
print('%.2f'%(num2))
print('%6.2f'%(num2))

print('%.0f%%입니다'%(12))       # %를 표시하는데 소수점없이...
print('12%입니다')



