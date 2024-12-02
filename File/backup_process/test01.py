import tomllib
import os
import sys
import log
import shutil
from datetime import datetime, timedelta
from distutils.dir_util import copy_tree
from DbConnect import DbConnect

 # 최초 실행시 설정 파일을 읽어서 전역변수 config에 설정한다.
try:    
    conf_file = "D:\\00.Dev\\PythonPorject\\File\\backup_process\\config.toml"        
    with open(conf_file, 'rb') as f:    
        config = tomllib.load(f)
except Exception as e:    
    print("파일 = " + conf_file)
    print(e)
    sys.exit(1)        

# 로그파일을 설정. 로그 생성위치를 지정한다.
logger = log.get_logger(name="BACKUP_MOVE")


# test

def main():    
    # logger.info(config)              
    logger.info('main_process')
    ip = config['DATABASE']['IP']
    dbname = config['DATABASE']['DB']
    uid = config['DATABASE']['UID']
    pw = config['DATABASE']['PW']   
    
    
    try:    
        db = DbConnect(ip, dbname, uid, pw)
        db.setLogger(logger)
        db.AdminUmsAlert(log_text='test메시지알림발송입니다.')
        db.BatchError(error_mesg='test용 에러 메시지 입니다.')
        db.BatchLog(ProcessNo=200, LogText='test실행 로그기록입니다.')
    except Exception as e:
        logger.info(e)


# main 시작점을 시작하게 한다.
if __name__ == "__main__":    
	main() 