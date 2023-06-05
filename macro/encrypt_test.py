import hashlib
import psutil
import log

logger = log.get_logger(name="TEST_LOG", log_dir="./logs")

# str1 = '{"VERSION":"1.0.0","ACNT_NO":12345,"CMD":"TEST","DATA1":"DATA11111"}'

# print(str1)
# print(hashlib.sha256(str1.encode()).hexdigest())

# str2 = 'upds://eyJWRVJTSU9OIjoiMS4wLjAiLCJBQ05UX05PIjoxMjM0NSwiQ01EIjoiVEVTVCIsIkRBVEExIjoiREFUQTExMTExIn0=/'
# print(str2)
# print(str2.split('//'))

# 실행중인 프로세스를 순차적으로 검색
for proc in psutil.process_iter():
    # 프로세스 이름을 ps_name에 할당
    ps_name = proc.name()
    # 실행 명령어와 인자(argument)를 리스트 형식으로 가져와 cmdline에 할당
    # cmdline = proc.cmdline()
    # print('NAME:', ps_name, ' CMD:', cmdline)
    logger.info('NAME:' + ps_name)