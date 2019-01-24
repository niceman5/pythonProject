# 이진 탐색 알고리즘
import bisect
seq = {0,1,2,2,4,5,6,7,8,9}
print('seq=', seq)
a = bisect.bisect_left(seq, 2)
# print('bisect.bisect_left(seq, 2)=', bisect.bisect_left(seq, 2))
# print('bisect.bisect_right(seq, 2)=', bisect.bisect_right(seq, 2))