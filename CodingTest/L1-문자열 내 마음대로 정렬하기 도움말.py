'''

입출력 예
strings	            n	return
[sun, bed, car]	    1	[car, bed, sun]
[abce, abcd, cdx]	2	[abcd, abce, cdx]


입출력 예 설명
입출력 예 1
sun, bed, car의 1번째 인덱스 값은 각각 u, e, a 입니다. 이를 기준으로 strings를 정렬하면 [car, bed, sun] 입니다.

입출력 예 2
abce와 abcd, cdx의 2번째 인덱스 값은 c, c, x입니다. 따라서 정렬 후에는 cdx가 가장 뒤에 위치합니다.
abce와 abcd는 사전순으로 정렬하면 abcd가 우선하므로, 답은 [abcd, abce, cdx] 입니다.

'''
from operator import itemgetter, attrgetter

def solution(strings, n):
    answer = []
    a = dict()
    for str in strings:
        a[str] = str[n]

    for key, value in sorted(a.items(), key=itemgetter(1)):
        answer.append(key)
    return answer

# def strange_sort(strings, n):
#     '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
#     return sorted(strings, key=lambda x: x[n])
#
# strings = ["sun", "bed", "car"]
# print(strange_sort(strings, 1))


#
# 메인 프로세스 시작
#
if __name__ == '__main__':
    # strList = ['sun', 'bed', 'car']
    # n = 1
    strList = ['abce','abcd','cdx']
    n = 2
    answer = solution(strList, n)
    print(answer)

