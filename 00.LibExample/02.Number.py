

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

print('{:->100}'.format(''))
# Decimal 은 사람을 염두에 두고 설계된 부동 소수점 모델에 기반하고, 필연적으로 최고 원리를 갖습니다 -- 컴퓨터는 사람들이 학교에서 배우는
# 산술과 같은 방식으로 동작하는 산술을 반드시 제공해야 한다.
# 수는 정확하게 표현할 수 있습니다. 반면에, 1.1과 2.2와 같은 수는, 이진 부동 소수점으로 정확히 표현할 수 없습니다. 최종 사용자는 일반적으로
# 이진 부동 소수점에서 그러하듯이 1.1 + 2.2 가 3.3000000000000003처럼 표시되는 것을 기대하지 않을 것입니다.
# 정확성은 산술에서도 유지됩니다. 십진 부동 소수점에서, 0.1 + 0.1 + 0.1 - 0.3 는 정확하게 0과 같습니다.
# 이진 부동 소수점에서, 결과는 5.5511151231257827e-017 입니다. 0에 가깝지만, 차이가 신뢰할 수 있는 동등성 검사를 방해하고, 차이는 누적
# 될 수 있습니다. 이러한 이유로, 강한 동등성 불변 조건을 갖는 회계 응용 프로그램에서는 decimal이 선호됩니다.

from decimal import *
a = Decimal('1')
print(a+1)
print(Decimal(10) / Decimal(3))
getcontext().prec = 8       # Decimal의 소수점을 적용한다.
print(Decimal(10) / Decimal(3))

getcontext().prec = 6
print(Decimal('3.1415926535') + Decimal('2.7182818285'))
getcontext().rounding = ROUND_UP        # 반올림 지정 해당 자리수
print(Decimal('3.1415926535') + Decimal('2.7182818285'))


print('{:->100}'.format(''))
import random
print(random.random())      # 0.0 ~ 1.0 사이의 float형을 얻는다.
print(random.randint(1,10)) # 해당 숫자 안의 수를 얻는다 int만 가능
print(random.uniform(1,10)) # x~y사이의 수치를 얻는다, float형
# random.seed(10)             # seed를 고정하여 난수 생성. 테스트시 동일한 난수값을 얻고 싶을때...없으면 시스템 시간으로 사용됨

l = [1,3,5,6,7,8,10,12]
print('random.choice=',random.choice(l))    # 시퀀스의 요소하나 반환
print('random.sample=',random.sample(l,2))  # 모집단 l에서 2개의 요소를 랜덤하게 구한다.
random.shuffle(l)                           # 요소 순서를 shuffle한다.


