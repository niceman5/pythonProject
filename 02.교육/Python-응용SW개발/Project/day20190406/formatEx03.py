
##
print('%d'%15)
print('{}'.format(15))

fruit = 'apple'
count = 10
print('제가 {0}를 {1}개 구입했습니다.'.format(fruit, count))
print('제가 {1}를 {0}개 구입했습니다.'.format(fruit, count))
print('제가 {1}를 {1}개 구입했습니다.'.format(fruit, count))

print('{0}'.format(2))
print('{0:5}'.format(2))    # 5자리 기본이 오른쪽 정렬
print('{0:<5}'.format(2))    # 5자리 왼쪽 정렬
print('{0:>5}'.format(2))    # 오른쪽
print('[{0:^5}]'.format(2))    # 가운데 정렬

print('{:.2f}'.format(3.141592))    # 소수 둘째자리까지 소수를 보여줘
