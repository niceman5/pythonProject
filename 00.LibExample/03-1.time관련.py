'''
시각관련
'''
import time

print(time.gmtime(), type(time.gmtime()))       # UTC현재시간을 표시한다.
print(time.localtime(), type(time.localtime())) # 지역의 현재시간을 표시한다.
print(time.strftime('%Y-%m-%d', time.localtime()))  # 날짜포멧으로 출력
print(time.time())



