# 아톰에서 한글처리시 반드시 포함해야 한다.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def student_score(**score):     # dict로 받음
    # for i in score.keys():
    #     print(i, score[i])
    tot = 0
    for key, value in score.items():
        print(key, value)
        tot += value

    print('합계 - {}'.format(tot))
    print('평균 - {}'.format(tot/len(score))) #길이가 변경됨으로 넘거진 인수갯수


# 함수 호출

student_score(kor=90, eng=100, math=95)


dic = {'name':'park'}
