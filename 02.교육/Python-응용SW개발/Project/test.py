# 주석 : 설명
# 변수 str선언
'''
설명 여러줄 주석
'''
"""
이것도 여러줄 주석
"""
str = 'hello'
print('str :',str)
print(type(str))
str = 10
print('str :',str)
print(type(str))
str = 2.34
print('str :',str)
print(type(str))

# 여러줄 문자열 
str2 = '''hello,
aaaaaa'''
print('str2 :',str2)
print(type(str2))

num1 = 10
num2 = 20
add =  num1 + num2
print('add :',add)
print('제곱 :',num1**2)
print('나눗셈 :',num1/num2)
print('몫 :',num1//num2)     #정수형태 몫
print('나머지 :',10 % 4)     #정수형태 몫


num1 = 10
num2 = 20
print('> :', num1 > num2)
print('== :', num1 == num2)
print('!= :', num1 != num2)

print('and:',10>3 and 5 > 2)
print('or:',10<3 or 5 < 2)
print('not:',not 10 < 5)
print('not:',not 0)     # 0이면 논리값 False False - not이니 True

