var = "Hello"

print('문자수:', len(var))
print('문자수:', len('hi~가'))
print('l갯수:', var.count('l'))
print('h갯수:', 'hi~ hi~'.count('h'))



var = "  Hello  "
print(var, len(var))
print('|'+var.lstrip()+'|')
print('|'+var.rstrip()+'|')
print('|'+var.strip()+'|')

var = "Hello"
print(var.lower())
print(var.upper())
print(var.find('e'))
print(var.index('e'))

# 찾는 문자가 없는경우
print(var.find('q'))        #없으면 -1이 됨
# print(var.index('q'))       #이건 에러남

print('a로 변경:', var.replace('el', 'a'))
print('문자열나누기:', var.split('l'))
print('문자열 삽입:', '~'.join(var))     #결과 확인

q = 'Time is too fast.'
print('q=',q)
idx = q.find('too')
print('too=',q[idx:idx+len('too')])
idx = q.find('fast')
print('fast=',q[idx:idx+len('fast')])


a = 'Pithon'
print(a)
# a[1]='y'   이렇게는 에러

print(a[:1] + 'y' + a[2:])
print(a.replace('i','y'))

