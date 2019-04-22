a = 3
b = 3
c = 3
print(a == b)
print(a is b)


import sys
print(sys.getrefcount(3))

## 변수 a는 3을 참조한다.
## b는 상수 3을 참조한다.

