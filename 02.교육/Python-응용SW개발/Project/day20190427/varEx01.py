num = 5

def increment():
    # num = 10
    global num      # 전역변수를 쓰게 한다.
    num = num + 1
    print('inner num', num)


increment()
print('outer num', num)
