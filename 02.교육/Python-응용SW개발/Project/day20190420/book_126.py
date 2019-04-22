##coffee = 10
##money = 300
##
##while money:
##    print('돈을 받으니 커피를 줍니다.')
##    coffee -= 1
##    print('남은 커피의 양은 {} 개'.format(coffee))
##    if not coffee:
##        print('커피가 다 떨어졌음...판매중지')
##        break
##
##print('실행완료')    




coffee = 10
while True:
    money = int(input('돈을 입력:'))
    if money == 300:
        print('커피준다')
        coffee -= 1
    elif money > 300:
        print('거스름돈 {}을 주고 커피주고'.format(money - 300))
        coffee -= 1
    else:
        print('돈을 다시 돌려주고 커피안줌')
        print('남은 커피는 {}개'.format(coffee))

    if not coffee:
        print('커피가 다 떨어졌음...판매중지')
        break
        
