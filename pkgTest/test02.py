from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(my_values, type(my_values))

print('Red:', my_values.get('red'))
print('Blue : ', my_values.get('blue'))
print('Green :', my_values.get('green'))
print('opacity :', my_values.get('opacity'))


print('opacity2 :', my_values.get('opacity', [''])[0] or 0)
print('opacity2 :', my_values.get('opacity', [''])[0])

# 손쉽게 짝홀수 그룹을 나눌수 있음
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[::2])
print(a[1::2])
