# import 파일명
# from 파일명 import 변수명, 함수명, 클래스
# import 파일명 as 별명

# [방법 1]
# import 모듈명
# import random
# print('random :', random.random())

# [방법 2]
# from 파일명 import 변수명, 함수명, 클래스
# from random import random
# print('random :', random())

# [방법 3]
# import 파일명 as 별명
# import random as r
# print('random :', r.random())

import random

print(random.uniform(1,10))
print(random.randrange(10))
print(random.randrange(1,100))
print(random.choice([2,4,6,8,10]))
