
num = 1     # 초기값

while num < 3: #조건식 : #반복할 조건 true일동안만 실
    #명령문
    print('num = {}'.format(num))
    num += 1        # 증감식

print('실행종료')



# 무한loop돌면서 조건으로 체크하는 방식이 있음
num = 1
while True:
    print('num = {}'.format(num))
    num += 1        # 증감식
    if num == 3:
        break

print('실행종료')


num = 1
while num < 11:
    num += 1
    if num % 2 == 0:    #짝수일때만 실행됨....skip된다.
        continue
    print('num = {}'.format(num))
