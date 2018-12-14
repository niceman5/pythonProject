'''
문제 설명
길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다.
입출력 예
n	return
3	수박수
4	수박수박
'''
'''
def water_melon(n):
    s = "수박" * n
    return s[:n]
    
    
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2


def water_melon(n):
    return ("수박"*n)[0:n]
    

'''
def solution(n):
    answer = '수박'
    if n / 2 == int( n / 2 ):
        answer = answer * int(n/2)
    else:
        answer = answer * int(n / 2) + answer[0]

    return answer
#
# 메인 프로세스 시작
#
if __name__ == '__main__':
    print(solution(11))
    print(solution(8))