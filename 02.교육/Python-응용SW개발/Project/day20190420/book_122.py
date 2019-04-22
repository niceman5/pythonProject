##treeHit = 0
##
##while treeHit < 10:
##    treeHit += 1
##    print('나무를 %d번 찍었습니다.' % treeHit)
##    if treeHit == 10:
##        print('나무넘어갑니다.')
##        


prompt = """
1. Add
2. Del
3. List
4. Quit

Enter Number : """

number = 0

while number != 4:
    number = int(input(prompt))

    if number == 1:
        print('1.Add')
        
    elif number == 2:
        print('2.Del')
        
    elif number == 3:
        print('3.List')        

    elif number == 4:
        print('4.Quit')        

    else:
        print('1,2,3,4만 입력하세요')

    print('-'*40)
