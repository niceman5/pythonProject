# 문제 5
num = int(input("정수 하나 입력 :"))

if num < 0 :
    print('0 미만')
               
elif num < 10:
    print('0 이상 10미만')
    
elif num < 20:
    print('10 이상 20미만')
    
elif num < 30:
    print('20 이상 30미만')
    
else:
    print('30 이상')
