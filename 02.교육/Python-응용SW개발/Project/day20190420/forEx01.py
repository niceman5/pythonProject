##data = [1,2,3]
##for n in data:
##    print(n)
##    
##
### string으로 loop가능
##for str1 in 'Hello':
##    print(str1)
##
##for n in range(1, 11):
##    print(n,end=' ')
##
####for 변수 in 리스트/튜플/문자열
##
####리스트 내포
####[명령문 for 항목 in 객체]
####[명령문 for 항목 in 객체 if 조건]
##
##[print(i) for i in range(1, 11)]
##[print(i) for i in range(1, 11) if i ==5]
##
##
##for n in range(10, 0, -1):  #끝값은 제외됨
##    print(n, end=' ')
##
##print('*'*50)
##[print(i) for i in range(1, 6) if i % 2 == 1]   #홀
##[print(i) for i in range(1, 6) if i % 2 == 0]   #짝
##
## 튜플로 만들어진 리스트도 가능
a = [(1,2), (3,4), (5,6)]

print('a의 자료형 : ' , type(a))
print('a[0]의 자료형 : ' , type(a[0]))

for n, m in a:
    print('n :{}, m :{}'.format(n, m))


for n in a:
    print('n[0]+n[1] :', n[0]+n[1])
    print('sum(n) =', sum(n))
