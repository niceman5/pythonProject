
# 매개변수에 *가 붙으면 리스트로 받음.
# 함수 호출시 인수를 안 넣어도 되고 1개 이상 넣을수 있다.
def sum_many(*args):
    sum = 0

    for i in args:
        sum = sum + i

    return sum


result = sum_many(1,2,3,4,5,6)
print(result)
result = sum_many()
print(result)
