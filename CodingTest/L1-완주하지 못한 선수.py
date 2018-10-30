'''

많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
입출력 예
participant	                            completion	            return
[leo, kiki, eden]	                    [eden, kiki]	        leo
예제 #1 leo는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

[marina, josipa, nikola, vinko, filipa]	[josipa, filipa, marina, nikola]	vinko
예제 #2 vinko는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

[mislav, stanko, mislav, ana]	[stanko, ana, mislav]	        mislav
예제 #3 mislav는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

'''

# def solution(p, c):
#
#     # c를 loop로 잡아 돌린다.
#     for c1 in c:
#         idx = p.count(c1)
#         if idx > 0:
#             p.remove(c1)
#     answer = p[0]
#     return answer

import collections


def solution(participant, completion):
    # collection의 Counter
    # 해시가능 객체를 계산하기 위한 dict서브 클래스 편리하고 빠른 기능 제공
    # list의 단어 갯수 세기나 특정파일에서 사용하는 가장 많은 단어 세기등.
    # list의 집합연산에 편하게 사용됨.



    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
#
# 메인 프로세스 시작
#
if __name__ == '__main__':

    # p = ['leo', 'kiki', 'eden']
    # c = ['eden', 'kiki']

    # p = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
    # c = ['josipa', 'filipa', 'marina', 'nikola']

    p = ['mislav', 'stanko', 'mislav', 'ana']
    c = ['stanko', 'ana', 'mislav', 'aaa']
    res = solution(p, c)
    print(res)

