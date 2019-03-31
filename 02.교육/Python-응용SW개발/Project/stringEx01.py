var = 'Hello'

#인덱싱 (문자하나)
print(var[0], var[1])
print('e출력:', var[1])
print('o출력:', var[4], var[-1])


#슬라이싱(연속된 문자)
print('el출력:', var[1:3])    #3이전까지 1부터 2까지가 됨
print(var[1:])


q = 'Time is too fast.'
print('too = ', q[8:11])
print('m = ', q[2])
print('fast = ', q[12:16])
print('fast = ', q[-5:-1])
