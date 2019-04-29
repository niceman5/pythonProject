##a = [(1,2),(3,4),(5,6)]
##
##for first, last in a:
##    print('first={} last={}'.format(first, last))
##
##
##for first in a:
##    print('first={} last={}'.format(first[0], first[1]))

##marks = [90, 25, 67, 45, 80]
##numbers = 0
##
##for mark in marks:
##    numbers += 1
##
##    if mark >= 60:
##        print('%d번째 학생은 합격입니다.'%(numbers))
##    else: 
##        print('%d번째 학생은 불합격입니다.'%(numbers))
##
##
### 132~133
##print('*'*50)
### enumerate로 
##for numbers, mark in enumerate(marks, 1):
##    
##    if mark < 60:
##        continue        # loop계속
##    print('%d번째 학생은 불합격입니다.'%(numbers))
##


marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print('%d번째 학생은 불합격입니다.'%(number+1))
