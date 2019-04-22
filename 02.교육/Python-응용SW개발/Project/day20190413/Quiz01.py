score = { 'hong':{'math':95, 'eng':85, 'kor':90},
          'park':{'math':85, 'eng':100, 'kor':80},
          'kim':{'math':75, 'eng':65, 'kor':100}
          }
# park의 모든 과목의 점수를 출력
print(score['park'])
# kim의 kor점수만 출력
print(score['kim']['kor'])

        
number=[100,200,100,500,200,600,300]
#요소값에서 중복제거하고 정렬하여 저장
lst = list(set(number))
lst.sort()
print(lst, lst.index(300))
lst.insert(lst.index(300)+1, 400)
print(lst)

j = '921103-1234567'

print(j[0:2])       #년 두자리
print(j[2:4])       #월 두자리
print(j[4:6])       #일 두자리
print(j[7:8])       #성별한자리
#j[2:4] = '08'       #안됨 상수는 변경안돰

print(j.replace('11', '08'))    #replace이용
print(j[0:2]+'08'+j[4:])

