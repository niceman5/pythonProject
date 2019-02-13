# 이진 탐색 알고리즘 -> 리스트에서 사용
import bisect
seq = [0,1,2,2,4,5,6,7,8,9]
print('seq=', seq)
a = bisect.bisect_left(seq, 2)
print('bisect.bisect_left(seq, 2)=', bisect.bisect_left(seq, 2))
print('bisect.bisect_right(seq, 2)=', bisect.bisect_right(seq, 2))
# 정렬된 상태를 유지하기 위해 검색된 위치에 삽입
bisect.insort_left(seq, 3)
print('bisect.insort_left(seq, 3)=', seq)
bisect.insort_right(seq, 5)
print('bisect.insort_right(seq, 5)=', seq)
print('{:->100}'.format(''))

# 수치배열을 효율적으로 다루는 array
# import array

# 열거형. 이름=값의 형태로 지정함. name과 value로 구성됨.
import enum
class Dynasty(enum.Enum):
    GOGURYE = 1
    BACKJAE = 2
    SILLA = 3
    GAYA = 4

d = Dynasty.SILLA
print(d)
print(d.name, d.value)
