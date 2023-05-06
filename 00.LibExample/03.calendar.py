import calendar

# 달력형태로 출력
calendar.prmonth(2023, 5)
# print(calendar.calendar(2023))

print(type(calendar.calendar(2023)))

# 요일출력
# 0	 1	2	3	4	5	6
# 월 화	수	목	금	토	일
print(calendar.weekday(2023, 5, 6))

# 요일출력시 
print('월화수목금토일'[calendar.weekday(2023, 5, 6)])

# 해당월 시작일과 마지막일자 
print(calendar.monthrange(2023, 2))

# 윤년관련 함수
print('2000년은 윤년인가?', calendar.isleap(2000))
print('2022년은 윤년인가?', calendar.isleap(2022))

# 특정기간동안의 윤년횟수를 계산
print('2020년부터 2024년까지 윤년 횟수', calendar.leapdays(2020, 2025))

# 2020년 3월 1일의 요일과 2020년 3월이 최대 몇일까지 있는지를 Tuple의 형태로반환합니다.
# 2020년 3월 1일은 6(일요일)이며, 2020년 3월은 31일까지 존재한다는 결과가 반환된 것을 볼 수 있습니다.
print(calendar.monthrange(2020, 3))