for num in [2,4,6,8]:
    print(num)
    
print('실행종료')

for i in range(1,3):
    print('바깥 loop : {}번째 실행'.format(i))
    for j in range(1,4):
        print('\t안쪽 Loop : {}번재 실행'.format(j))
        

for i in range(2, 10):
    for j in range(1, 10):
        print('{} * {} = {}'. format(i, j, i*j))
    print('')
    

# 짝수만
for i in range(2, 10, 2):
    for j in range(1, 10):
        print('{} * {} = {}'. format(i, j, i*j))
    print('')
    

# 단까지만 반복
# 방법1
for i in range(2, 10, 2):
    for j in range(1, i+1):
        print('{} * {} = {}'. format(i, j, i*j))
    print('')

# 방법2    
for i in range(2, 10, 2):
    for j in range(1, 10):
        print('{} * {} = {}'. format(i, j, i*j))

        if i == j:
            break       #반복문 탈출
    print()
