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
print('{:->100}'.format(''))
perfs = {
    '가나다':'123',
    '나다라':'2222',
    '다라마':'2223',
    '라마바':'3333'
}
print(perfs)
print(list(perfs.items()))

import pprint
pprint.pprint(perfs)
pprint.pprint(list(perfs.items()))

print('{:->100}'.format(''))
# 여러개의 iterable객체를 연결한 반복자를 만듬
import itertools
it = itertools.chain([1,2,3], {'a','b','c','b'})
for v in it:
    print(v, ' ', end='')
print()
print('{:->100}'.format(''))
iters = ([1,2,3], {'a','b','c','b'})
for c in itertools.chain.from_iterable(iters):
    print(c, ' ', end='')
print()
print('{:->100}'.format(''))

# 값의 순열,조합 구하기. ABC로 조합되는 순열
for v in itertools.permutations('ABC',2):
    print(v)
print('')
print('{:->100}'.format(''))
for v in itertools.combinations('ABC',2):
    print(v)
print('')
print('{:->100}'.format(''))
for v in itertools.combinations_with_replacement('ABC', 2):
    print(v)

print('')
print('{:->100}'.format(''))
#
for v in itertools.product('ABC', [1,2,3]):
    print(v)

# iterable 객체의 필터링
def is_even(n): # n이 짝수면 True를 리턴
    return n % 2 == 0

for v in filter(is_even, [1,2,3,4,5,6,7]):
    print(v)
# function에 None을 지정하면 객체에서 참인값만을 반환
items = [1, 0, 'Spam', '', [], [1], [2]]
for v in filter(None, items):
    print(v)
print(v)
print('{:->100}'.format(''))
# data와 selections 두개의 iterable객체를 지정하며 selections에서 얻은 값이 True면 data에서 얻은 같은 순번의 값을 반환
for v in itertools.compress(['spam', 'egg', 'ham', '김치', '멸치'], [1,0,0,1,1,1,1]):
    print(v)
print(v)
print('{:->100}'.format(''))

# 등차수열 만들기
for v in itertools.count(1, 3): # 초기값,값의 공차
    if v > 10: break
    print(v, ' ', end='')
print(v)
print('{:->100}'.format(''))

# 지정한 값을 반복, 반복횟수에 None이면 무한반복
print(list(itertools.repeat('a',5)))
print(list(itertools.repeat('ab',5)))
print('{:->100}'.format(''))

# 지정한 iterable객체의 모든값을 반복하는 반복자를 생성
for v in itertools.islice(itertools.cycle('abc'),0,5):
    print(v)
print(v)
print('{:->100}'.format(''))

# 여러 iterable객체의 요소로 튜플만들기. 객체중 하나가 값을 모두 반환하면 종료됨. 모든 객체로 부터 생성하려면 zip_longest사용
for v in zip((1,2,3,4), ('a','b','c','d'), ('가','나','다')):
    print(v)
print(v)
for v in itertools.zip_longest('abcdefg', '123', '가나다라마바', fillvalue='-'):
    print(v)
print(v)

print('{:->100}'.format(''))