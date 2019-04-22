
n = int(input('보고싶은 구구단:'))
for i in range(1, 10):
    print('{} * {} = {}'.format(n, i, n*i))

n = sum( range(1, 11) )
print('1~10 누적합:', n)

n = 0
for i in range(1,11):
    n += i
print('1~10 누적합:', n)    



n = 1
for i in range(1,6):
    n = n * i
print('5! = ', n)


lst = [i for i in range(1, 101) if i % 3 == 0]
print(lst)
print(len(lst))
