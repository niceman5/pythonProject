##a = [1, 2]
##b = [3, 4]
##a.extend(b)
##print(a)

## 문제
## 'hi'요소를 찾아 'hello'로 변
data = [100, 200, 'hi', 'good', 300]
print(data)
data[data.index('hi')] = 'hello'
print(data)


a = [1,2,['a','b',['life','is']]]
print(a)
print(a[2][2][0])

a = [1, 2, 3]
print(a[2] + 'hi')
