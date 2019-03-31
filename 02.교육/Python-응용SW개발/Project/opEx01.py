# 삼항연산자.
# 조건 먼저 판단하고 실행
print('크다' if 5 > 3  else '작다')
print('크다' if 5 < 3  else '작다')

# 변수 num의 값이 10이면 변수 var에 num의 값을 저장
# 그렇지 않다면 var에 -1을 입력

num = 10
var = num if num == 10 else -1 

print('var : ', var)


# n1과 n2를 비교해서 큰 값을 result에 저장
n1 = 20
n2 = 15
result = n1 if n1 > n2 else n2
print('result : ', result)

#n1값이 양수면 '양수'를 value에 n1이 0또는 음수면 '0또는 음수'
n1 = 0
value = '양수' if n1 > 0 else '0 또는 음수'
print('value : ', value)
