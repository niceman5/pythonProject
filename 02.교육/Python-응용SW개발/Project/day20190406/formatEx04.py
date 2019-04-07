## 서식문자 %c

# ch = 'a'
ch = 98

print('문자 값:%c'%ch)
print('문자 값:%s'%ch)

print("[%10s]"%('hi'))
print("[%10sjane]"%('hi'))
print("[%-10sjane]"%('hi'))

fruit = 'apple'
count = 10
print('제가 {name}를 {cnt}개 구매입했습니다.'.format(name=fruit, cnt=count))
print('{0:<10}'.format('hi'))
print('{0:>10}'.format('hi'))
print('{1:^10}'.format('hi','aaa'))
print('{1:0^10}'.format('hi','aa'))
print('{1:*^10}'.format('hi','aa'))     # 서식은 0만 되는데 포멧은 다른 문자도 가능

print('포멧함수는 {{}}를 {{ 사용'.format())    # %를 찍기위해 %%와 동

