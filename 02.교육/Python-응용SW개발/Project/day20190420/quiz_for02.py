####수학점수가 60점 이상인 학생번호와 점수 출력
##m = [90,45,60,75,50]
##
### print(m)
##
##for idx in range(len(m)):
##    if m[idx] >= 60:
##        print('{}번째 학생은 {}점으로 합격'.format(idx+1, m[idx]))
##    
##print('-'*50)
##
##for idx, score in enumerate(m):
##    if score >= 60:
##        print('{}번째 학생은 {}점으로 합격'.format(idx+1, score))
##
##print('-'*50)        
### 한줄로,,,,
##[print('{}번째 학생은 {}점으로 합격'.format(idx+1, score)) for idx, score in enumerate(m) if score >= 60]
##
##print('-'*50)


##수학점수가 60점 이상인 학생이름과 점수 출력
m = {'일길동':90, '이길동':45, '삼길동':60, '사길동':75, '오길동':50}

for name in m :
    #print(name)
    if m[name] >= 60:
        print('{}학생은 {}점으로 합격'.format(name, m[name]))

for item in m.items():
    if item[1] >= 60:
        print('{}학생은 {}점으로 합격'.format(item[0], item[1]))

for key, value in m.items():
    if value >= 60:
        print('{}학생은 {}점으로 합격'.format(key, value))
