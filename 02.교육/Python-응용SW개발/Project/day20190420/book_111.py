##money = 2000
##card = 1
##
##if money >= 3000 or card:
##    print('A')
##else:
##    print('B')

print(5 in [1,2,3])

dic = {'name':'kim', 'phone':'010-111-1111', 'addr':'강남'}

print('phone' in  dic)  #key는 찾음
print('kim' in  dic)    #value는 ? 안됨
print('kim' in dic.values())
print('y' in 'python')      # 문자열에 속하는지 확인
