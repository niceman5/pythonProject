'''
date    일자다루기
time    시간다루기
datetime    일시다루기
timedelta   두 일시의 차 다루기
'''
from datetime import date       # 날자를 다루는 date

newyearsday = date(2019, 1, 10)     #지정한 날짜의 date 객체를 생성하는 생성자.
print(newyearsday, type(newyearsday))
print(newyearsday.weekday())        # 월요일을 0, 일요일을 6으로 하여 요일 반환
print(newyearsday.isoweekday())     # 월요일을 1, 일요일을 7으로 하여 요일 반환
print(newyearsday.isoformat(), type(newyearsday.isoformat()))      # YYYY-MM-DD로 리턴 str로
print(str(newyearsday), type(str(newyearsday)))     # date객체에서 날자 구하기
print(newyearsday.strftime('%Y/%m/%d'))     # 날짜를 /로 들어간 문자로 ..
print(newyearsday.strftime('%Y %b %d (%a)'))    # 날짜를 월, 요일이 포함된 문자열로 표시
print(date.today(), type(date.today()))         # 당일을 구한다.
print(newyearsday.year, newyearsday.month, newyearsday.day)     # 년월일 값을 반환. 모두 int형으로 리턴됨


print('{:->100}'.format(''))
from datetime import time       # 시간을 다루는 time
print(time(), time(20, 50, 51))     # 시간을 지정하여 시간 객체 생성
print(time(minute=15))              # 분 지정, 15분
now = time(17,22,10)
print(now.hour, now.minute, now.second, now.microsecond)    # 시,분,초를 리턴, 모두 int형으로 리턴됨.
print(now.isoformat(), type(now.isoformat()))               # 문자열
print(now.strftime('%H:%M:%S'))        #시간을 문자열로 출력


print('{:->100}'.format(''))
from datetime import datetime   # 일시를 다루는 객체
today = datetime.today()
print(today.date(), type(today.date()))
print(today.time(), type(today.time()))
print(today.isoformat())
print(today.strftime('%Y-%m-%d %H:%M:%S'))      #출력

print('{:->100}'.format(''))
from datetime import datetime, date, time, timedelta    # 일시의 차 - timedelta개체
today = date.today()
date1 = date(2019, 1, 1)
print(today, date1)
print(date1 - today, type(date1 - today))       # 두일자의 차이
week = timedelta(days=7)                        # 일주일 뒤의 timedelta를 생성
print(week, type(week))
print(today+week, type(today+week))             # 일시를 더한다. 일주일뒤
print(today+week*2)         # 2주뒤
print(today-week, type(today-week))         # 일주일전



