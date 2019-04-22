#튜플


a = [1,2,3]     # 리스트
print(type(a), a)

b=(1,2,3)
print(type(b), b)

#b[0] = 10      # 튜플은 변경안됨/수정/삭제도 안됨


#튜플 선언
touple1 = ()    # 빈 튜플
touple2 = (1)
touple3 = (1,(2,3))

print(type(touple1), type(touple2))
print(type(touple3), touple3)

a = 1, 2
print(type(a), a)
a , b = 1, 2
print(type(a), a)
print(type(b), b)

a = 1, 2
b = 3, 4
print(a + b)
print(a * 3)
