

print('abs(-5.0)=', abs(-5.0), ' ', 'abs(15.0)=', abs(15.0))    # 절대값
print(max(1,-2,5))
print(min(1,-2,5))
print(sum([1,2,5]))         # 합계
print(sum([1,2,3],-1))      # start=2일때
print(pow(2,3))             # 2의 3 승
print(pow(2,3,6))           # 2의 3승에서 % 6 .... 6으로 나눈 나머지


import math
print('{:->100}'.format(''))
print( math.ceil(3.14))     # 부동소수점 x값 이상의 최소 정수값을 구한다
print(math.floor(3.14))     # 부동소수점 x값 이하의 최대 정수값을 구한다
print(math.trunc(3.14))     # 부동소수정 x값 소수점 이하를 버린다.
print(math.fabs(-3.14))     # 부동소수정 x값의 절대값을 구한다.

print('{:->100}'.format(''))
print('연산자와 내장 함수 차이')
print(math.pow(2,3))            # 두개의 인수가 int여도 반환값은 float
print(pow(2,3))                 # 내장함수일때 반환값은 int
print(2**3)                     # 연산자일때 반환값은 int
print(pow(2,3.0))               # 내장함수라도 int float형을 주면 반환값은 float형

