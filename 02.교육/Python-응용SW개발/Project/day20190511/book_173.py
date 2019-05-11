result = 0

def adder(num):
    global result   # result변수가 global변수인지 선언하는것..할당은 안됨
    result += num
    return result


print(adder(3))
print(adder(4))
