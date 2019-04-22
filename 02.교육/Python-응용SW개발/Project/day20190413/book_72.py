a = [1,2,3]
print(type(a), a)
a[2] = 4
print(a)
print(a[1:2])
#a[1:2] = ['a','b','c']  #리스트가 교체됨


print( 'type(a[1:2]):', type(a[1:2]))   #결과는 리스트
print( 'type(a[1]):', type(a[1]))       #결과는 int

a[1] = ['a','b','c']    #리스트에 리스트가 들어감
print(a)
a[1:2] = []
print(a)
del a[0]
print(a)
a.append(6)
print(a)
#a.append([5,6])
a.append(2)
a.append(1)
print(a)
a.sort()
print(a)

##han = ['가','나','다','가','황',]
##
##han.reverse()   #오름차순 먼저하고 내림차순해야 한다.
##print(han)
##han.sort()
##print(han)
##han.reverse()   #오름차순 먼저하고 내림차순해야 한다.
##print(han)


print(a.index(4))
#print(a.index(0))       #에러
a.insert(1,5)
a.insert(0,10)
print(a)
a.append(4)
print(a)
a.remove(4)         #지우고자 하는 값을 지정
print(a)
#a.remove(11)        #없는값삭제시 에
b = a.pop()         #가장뒤의 데이터를 꺼내온다. 삭제.
print(b, a)
cnt = a.count(6)
print(cnt)  
#a.extend([20,30])   # 리스트의 확장
a= a + [20,30]      #동일한 결과 
print(a)
