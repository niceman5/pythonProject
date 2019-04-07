## 출력형태 지정
## 문자 : a
## 문자열 : abc

fruit = 'apple'
count = 10

print('fruit:',fruit)
print('과일', fruit, '를', 10, '개 구입')
print('과일 %s를 %d개 구입'%(fruit, count))

# 문제
name = '홍길동'
age = 25

## 제 이름은 홍길동이고 나이는 25세 입니다.
print('제 이름은 %s이고 나이는 %d세 입니다.'%(name, age))

pi = 3.141592
p2 = 3.6
print('%f %d %d %.2f'%(pi, pi, p2, pi))     # 소수점 2째자리까지 %.2f
