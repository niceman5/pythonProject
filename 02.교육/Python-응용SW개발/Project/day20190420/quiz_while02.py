## 문제
##1번째 : <1 이상 정수 입력> :10
##2번째 : <1 이상 정수 입력> :32
##3번째 : <1 이상 정수 입력> :55
##4번째 : <1 이상 정수 입력> :20
##5번째 : <1 이상 정수 입력> :2
##누적합 : 119 
##입력값 모두 출력 : [10, 32, 55, 20, 2]

cnt = 1
lst = []

while cnt < 6:
    print('{}번째 : <1 이상 정수 입력> :'.format(cnt), end='')
    cnt += 1
    num = int(input())    
    lst.append(num)

print('누적합 : {} '.format(sum(lst)))
print('입력값 모두 출력 :' , lst)
