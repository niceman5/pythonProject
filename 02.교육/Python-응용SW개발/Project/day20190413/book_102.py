import sys
from copy import copy


a, b = ('python', 'life')
print(type(a), a)
print(type(b), b)
a, b= b, a  #값을 서로 바꿈,.,.swap
print(type(a), a)
print(type(b), b)



(a,b) = 'python', 'life'
print(type(a), a)
print(type(b), b)

[a,b] = ['python', 'life']
print(type(a), a)
print(type(b), b)

a = b = 'python'
print(type(a), a)
print(type(b), b)

print(sys.getrefcount('python'))

n1 = 3
n2 = 5
print('n1={}, n2={}'.format(n1,n2))

lst1 = [1,2,3]
lst2 = lst1             #같은 주소를 가르킴
print(lst1, lst2)
print(lst1 is lst2)

lst1[1]=200     # lst1 lst2동시에 바뀜
print(lst1, lst2)

lst2 = lst1[:]          # 새로운 주소를 생성.....독립적으로 사용되게 하려면 이 방법을 사용
lst2 = copy(lst1)       # copy를 아용할수 있음,,,,


