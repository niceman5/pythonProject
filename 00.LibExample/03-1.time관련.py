'''
시각관련
'''
import time

print(time.gmtime(), type(time.gmtime()))       # UTC현재시간을 표시한다.
print(time.localtime(), type(time.localtime())) # 지역의 현재시간을 표시한다.
print(time.strftime('%Y-%m-%d', time.localtime()))  # 날짜포멧으로 출력
print(time.time())

print('{:->100}'.format(''))
local = time.localtime()
utc = time.gmtime()

print('local.tm_mday=', local.tm_mday)
print('local.tm_hour=', local.tm_hour)
print('utc.tm_hour=', utc.tm_hour)


# print('{:->100}'.format(''))
# for i in range(10):
#     print(time.time())
#     time.sleep(0.5)     # 0.5초를 sleep 한다. 스레드를 지정한 시간동안 sleep한다.
#

#
# 파이선 datetime확장모듈 설치
# pip install python-dateutil
#
print('{:->100}'.format(''))

import dateutil.parser

dt = dateutil.parser.parse('2019-01-14 15:22:22')
print(dt.strftime('%Y-%m-%d %H:%M:%S'))
dt = dateutil.parser.parse('20180623')
print(dt.strftime('%Y-%m-%d %H:%M:%S'))
dt = dateutil.parser.parse('20180623112546')
print(dt.strftime('%Y-%m-%d %H:%M:%S'))
dt = dateutil.parser.parse('Tue, 23 Jun 2015 12:34:56 GMT')
print(dt.strftime('%Y-%m-%d %H:%M:%S'))
# dt = dateutil.parser.parse('Tue, 23 Jun 2015 12:34:56 KST')       tzname KST identified but not understood
# print(dt.strftime('%Y-%m-%d %H:%M:%S'))


print('{:->100}'.format(''))
# 날짜의 차이를 계산
from dateutil.relativedelta import relativedelta
from datetime import datetime, date
now = datetime.now()    # 현재 일시를 얻음
today = date.today()    # 현재 날자를 얻음
print('한달후=',now+relativedelta(months=+1))     # 한달후
print('한달전의 일주일전=',now+relativedelta(months=-1, weeks=+1))   # 한달전의 일주일전
print('한달후 10시=', today+relativedelta(months=+1, hour=10))  # 한달후 10시   10시지정

print('{:->100}'.format(''))
# 요일 지정
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
print('다음 금요일=',today+relativedelta(weekday=FR))      # 다음 금요일  요일 계산처리
print('이번달의 마지막 금요일=', today+relativedelta(day=31, weekday=FR(-1)))  # 이번달의 마지막 금요일
print('다음 화요일=', today+relativedelta(weekday=TU(+1)))
print('오늘을 제외한 다음 화요일=', today+relativedelta(days=+1, weekday=TU(+1)))  #오늘이 화요일이여도 무조건 다음주 화요일

print('{:->100}'.format(''))
print('2015년의 100일째 =', date(2015, 1, 1)+relativedelta(yearday=100))
print('2015년의 100일째(날짜상관없이 연도부터 센다) =', date(2015, 10, 11)+relativedelta(yearday=100))
print('2012년 100일째=', date(2012,1,1) + relativedelta(yearday=100))
print('2012년 윤일제외한 일자=', date(2012, 1, 1) + relativedelta(nlyearday=100))
print(relativedelta(date(2015, 1, 1), today))

print('{:->100}'.format(''))
# rrule은 달력 어플등에서 반복을 지정하기 위해 자주 사용,
from dateutil.rrule import rrule
from dateutil.rrule import DAILY, MONTHLY, WEEKLY
import pprint
import sys
sys.displayhook = pprint.pprint
start = datetime(2015, 6, 28)
print('지정일로 부터 5일=', list(rrule(DAILY, count=5, dtstart=start)))
print('지정기간 매일=', list(rrule(DAILY, dtstart=start, until=datetime(2015, 7, 1))))
print('매주 화,목=', list(rrule(WEEKLY, count=8, wkst=SU, byweekday=(TU, TH), dtstart=start)))
print('매월 마지막 금요일=', list(rrule(MONTHLY, count=3, byweekday=FR(-1), dtstart=start)))
print('격주=', list(rrule(WEEKLY, interval=2, count=3, dtstart=start)))





