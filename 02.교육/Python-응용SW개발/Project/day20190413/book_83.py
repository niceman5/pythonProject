a = {1:'hi', 2:'hello', 'name':['kim', 'park','lee'], }
print(a)
print(a[1])
print(a['name'][1])
a[3]='b'        # dic에 추가
print(a)

##del a[1]
##print(a)
print(a.keys())

for k in a.keys():
    print(k)

print(a.items())
it= list(a.items())
print(type(it[0]), it[0])

##정수 -> 논리값
##0   -> False
##0이외 -> True
##
##논리값 -> 정수
##False -> 0
##True  -> 1
