# 구구단 2단
num = int(input("몇단? : "))
cnt = 1

while cnt < 10:
    print('{} * {} = {}'.format(num, cnt, num*cnt))
    cnt += 1
    


# 누적합

num = int(input("누적 반복 카운트 : "))
loop = 0
cnt = 0

while loop < num:    
    loop += 1
    cnt = cnt + loop
    print('현재값 {}, 누적값 {}'.format(loop, cnt))

print('{} ~ {} 누적합 : {}'.format(1, num, cnt))    

