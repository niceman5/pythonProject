"""가변인수 처리를 깔끔하게 보이게
"""
from datetime import datetime, time
import time
def log(mesg, values):
    if not values:
        print(mesg)
    else:
        values_str = ", ".join(str(x) for x in values)
        print("%s : %s" % (mesg, values_str))

def log2(mesg, *values):
    if not values:
        print(mesg)
    else:
        values_str = ", ".join(str(x) for x in values)
        print("%s : %s" % (mesg, values_str))

# 인수 기본값 지정. 이게 제일 좋은거 같음 
def log3(mesg="", mesg2="", mesg3=""):
    print(mesg+mesg2+mesg3)

# 시간값을 찍는 로그함수. 문제가 datatime.now()는 함수를 정의할때 한번만 실행됨
# 이 모듈이 로드된 이후는 같은 시간만 찍힘
# 인수값에 값 지정시 한번만 평가되니 이점 반드시 유의해야 함
def log_time(mesg="", when=datetime.now()):
    print("%s : %s" % (when, mesg))

def log_time2(mesg="", when=None):
    when = datetime.now() if when is None else when
    print("%s : %s" % (when, mesg))
    
    
    
    
log("My Numer is", [1,2,3])
# 두번째 인수는 없는데도 반드시 넘겨야 함
log("Hi 인수는없음!", [])


log2("2 My Numer is", [1,2,3])        
log2("2 Hi 인수는없음!")        # 이게 훨씬 나음.

favorites = [7, 13, 99]
log("favorites colors", favorites)


# 인수가 여러개 있을경우 이 방법도 좋음.
log3(mesg="반가워요")
log3(mesg3="반가워요3")

log_time("시간체크11")
time.sleep(1)
log_time("시간체크12")

log_time2("시간체크21")
time.sleep(1)
log_time2("시간체크22")

