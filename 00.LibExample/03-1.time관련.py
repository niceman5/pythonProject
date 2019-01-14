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










