n1 = 10
n2 = 2.24

print(type(n1))
print(type(n2))

# 8진수
n3 = 0o10
print(type(n3))
print(n3)

# 16진수
n4 = 0x10
print(type(n4))
print(n4)

#이스케이프 코드
print('hi~\nhi~')
print('hi~\t\'hi~\'')   # tab과 '출력
print("hi~'hi~'")
print('hi~"hi~"')

str1 = 'hi~ hi~'
print(str1)
str2 = "hi~ hi~"
print(str2)
str3="""
I said,
"Good bye".
"""
print(str3)
print(str1+str2)
print((str1+'!!') * 2)
# print(str1+2) 에러남
print(str1+str(2))

two = str(2)
print(type(two))

str_two = '2'
print(type(str_two))
print(type(int(str_two)))


str1 = 'hi~ hi~'
print(('hi~ hi~'+'\n')*3)


print('='*20)
print('my rogram')
print('='*20)
