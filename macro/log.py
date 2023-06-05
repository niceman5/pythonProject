### log를 세팅 해주는 단계입니다.

'''
Log Levels
로그는 아래 목록 중 하나의 레벨을 가지며, 각 레벨의 로그는 각기 다른 용도를 지니고 있다.

DEBUG: 프로그램 작동에 대한 상세한 정보를 가지는 로그. 문제의 원인을 파악할 때에만 이용.
INFO: 프로그램 작동이 예상대로 진행되고 있는지 트래킹하기 위해 사용.
WARNING: 예상치 못한 일이나 추후 발생 가능한 문제를 표시하기 위함.
ERROR: 심각한 문제로 인해 프로그램이 의도한 기능을 수행하지 못하고 있는 상황을 표시.
CRITICAL: 더욱 심각한 문제로 인해 프로그램 실행 자체가 언제라도 중단될 수 있음을 표시.

로그 찍히는 레벨은 해당 레벨이상만 찍힘
즉 debug는 모두 찍는데 반해 info로 하면 debug는 안 찍힘
'''
import logging
import datetime
import os

def get_logger(name=None, log_dir="./logs"):
    #1 logger instance를 만듭니다. 
    logger = logging.getLogger(name)
    
    #1-1 로그가 생성될 디렉토리를 검사하고 없으면 생성한다.
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    
    #2 logger의 level을 가장 낮은 수준인 DEBUG로 설정합니다.
    logger.setLevel(logging.DEBUG)
    
    #3 formatter 지정하여 log head를 구성해줍니다. 
    ## asctime - 시간정보
    ## levelname - logging level
    ## funcName - log가 기록된 함수
    ## lineno - log가 기록된 line    
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - [%(funcName)s:%(lineno)d] - %(message)s")
    
    #4 handler instance 생성하여 console 및 파일로 저장할 수 있도록 합니다. 파일명은 txt도 됩니다.
    # console = logging.StreamHandler()
    file_handler_debug = logging.FileHandler(filename=log_dir+'/log{:%Y%m%d}_debug.log'.format(datetime.datetime.now()))
    file_handler_info = logging.FileHandler(filename=log_dir+'/log{:%Y%m%d}_info.log'.format(datetime.datetime.now()))
    
    #5 handler 별로 다른 level 설정합니다. 설정한 level 이하 모두 출력,저장됩니다.
    # console.setLevel(logging.INFO)
    file_handler_debug.setLevel(logging.DEBUG)
    file_handler_info.setLevel(logging.INFO)

    #6 handler 출력을 format 지정방식으로 합니다.
    # console.setFormatter(formatter)
    file_handler_debug.setFormatter(formatter)
    file_handler_info.setFormatter(formatter)

    #7 logger에 handler 추가합니다.
    # logger.addHandler(console)
    logger.addHandler(file_handler_debug)
    logger.addHandler(file_handler_info)
	
    #8 설정된 log setting을 반환합니다.
    return logger    