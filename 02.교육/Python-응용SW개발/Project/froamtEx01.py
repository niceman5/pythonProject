n1 = 10
n2 = 20
print('n1:',n1,'n2=',n2)
print('n1=%d, n2=%d'%(n1,n2))   # 서식문자가 2개이상이면 소괄호를 사용해야 한다.
print('%d'%n1)      #왼쪽 정렬
print('%5d'%n1)     #자리수가 정해지면 오른쪽 정렬
print('%-5d'%n1)    #왼쪽정렬옵션

print()
print('사과 %d개'%12)
apple = 212
print('사과 %d개'%apple)
pear = 551
print('사과 %d개, 배 %d개'%(apple,pear))

f1 = '사과'
f2 = '배'
print('%s 2개'%f1)

print('형태 %s %d개, %s %d개'%(f2, pear, f1, apple))
