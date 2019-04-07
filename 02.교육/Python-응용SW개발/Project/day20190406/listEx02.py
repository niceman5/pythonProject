

##a = [1, 2]
##b = [3, 4]
##
##print(a+b)
##print(a*3)
##a = a * 3
##print(a)
##a[1] = 100
##print(a)
##
### 여려개의 요소를 한번에 변경
##a[2:4] = 200,300
##print(a)
##
### 요소를 삭제하는 효과가 있음....
##a[2:4] = []
##print(a)
##
##a[0] = [50]
##print(a)
##
##
##a[0] = 50
##print(a)
##
##a.sort()
##print(a)
##
##a.reverse()
##print(a)


a = ['one','two','three']
print(a)
a.append(100)
print(a)
##a.append(200)
##print(a)
a = a + [200,300]
print(a)

a.insert(3, 'four')
print(a)
print(a.count(100))
