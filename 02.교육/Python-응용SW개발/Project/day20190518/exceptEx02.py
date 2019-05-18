try:
    4 / 0
# except ZeroDivisionError as e:
except FileNotFoundError as e:
    print(e)
    print('error')

print('success~~~~')
