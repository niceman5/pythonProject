s1 = set([1, 2, 3, 1])
print(type(s1), s1)

s2 = set('Hello')       # 중복된 데이터가 있음 제거한다.
print(type(s2), s2)

s1.add(4)
print(s1)
s1.update([4,5,6,1,2,3])
print(s1)
#s1.remove(10)       #없으면 에러
s1.remove(2)
print(s1)

s1 = set([1,2,3,4])
s2 = set([1,2,5,6])
print(s1, s2)
print('교집합:', s1&s2)    #교집합
print('교집합:',s1.intersection(s2))

print('합집합:', s1|s2)
print('합집합:', s1.union(s2))

print('차집합:', s1-s2)
print('차집합:', s2-s1)

