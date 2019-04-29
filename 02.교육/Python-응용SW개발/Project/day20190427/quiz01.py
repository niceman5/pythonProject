def four_rules(a, b):
    print('{} + {} = {}'.format(a, b, a+b) )
    print('{} - {} = {}'.format(a, b, a-b) )
    print('{} * {} = {}'.format(a, b, a*b) )
    print('{} / {} = {}'.format(a, b, a/b) )

def star_count(cnt):
    print('*'*cnt)

def accumulator(a, b):
    re = 0
    # if a > b:
    #     a, b = b, a
    max, min = (a, b) if a > b else (b, a)  # 값이 하나만 와야 함
    re = sum( range(min, max+1) )

    # re = sum( range(a, b+1) )
    return re
# four_rules(7, 2)
# star_count(7)

print(accumulator(1, 10) )
print(accumulator(10, 1) )
