"""
backup파일을 관리하는 프로세스

[ROOT]의 의 위치에 db백업이 실시간으로 이루어진다.
 - FULL 백업 : DATABASE전체 백업및 로그백업
    --> 1일 1회 : 04시에 전체 배업됨
 - DIFF(차등) 백업 : FULL백업이후의 DB의 증감분만 백업
    --> 1시간마다 실행됨    
 - LOG 백업 : 차등백업이후 transaction의 기록임
    --> 10분단위 실행됨

- 백업복원시 처리방법은 
    마지막일자의 FULL백업 + 
    마지막시간의 DIFF백업 + 
    마집막시간 DIFF이후의 LOG백업들
    
* 백업파일 처리방법
1) 이 배치는 05시에 실행된다    
2) 05시에 현재 04시 FULL백업 이전에 생성된 백업파일들 삭제한다.
3) 현재일의 FULL백업을 일자별 백업에 복사한다.
4) 모든 과정은 LOG파일에 기록을 남긴다.

작성자 : UCRM 김태훈
작성일 : 2023-05-01

수정이력)
"""
import tomllib
import os
import log
import datetime

logger = log.get_logger()

# 설정값을 읽는다.
def config_read():    
    # with open("E:\\pythonProject\\File\\backup_process\\config.toml", "rb") as f:
    with open('D:\\00.Dev\\PythonPorject\\File\\backup_process\\config.toml', "rb") as f:
        config = tomllib.load(f)
    
    logger.info("CONFIG FILE READ")        
    return config    

# main함수
def main():
    config = config_read()  # 전역변수사용    
    logger.info(config)              
    logger.info('main_process')
    
    root_path = config['ROOT']['PATH']      # 백업파일이 있는 path
    daily_path = config['DAILY']['PATH']    # 일자별 full 백업이 복사될 path
    base_dt = '{:%Y%m%d}'.format(datetime.datetime.now()) + '_040000'    
    # test용코드 
    base_dt = '20230502_041000'
    logger.info(root_path)
    
    # 전체 파일 리스트를 구한다.
    file_full_list = os.listdir(root_path)
    file_list = []
    
    # BAK인 목록과 TRN목록을 구해 통합 리스트를 만든다.
    file_list += [file for file in file_full_list if file.endswith(".BAK")]    
    file_list += [file for file in file_full_list if file.endswith(".TRN")]
    logger.info('전체 파일 리스트 ')
    logger.info(file_list)
    logger.info('처리 기준일시 :' + base_dt)
    for file_name in file_list:        
        name1 = file_name.split("(")
        name2 = name1[1].split(")")
        logger.info("처리대상 파일명 : %s  날짜값 : %s" % (file_name, name2[0]) )
        
        
    
    
    # for file_name in os.listdir(root_path):
    #     logger.info(file_name)
    #     if file_name.endswith('.BAK') or  file_name.endswith('.TRN'):
            
        


# main 시작점을 시작하게 한다.
if __name__ == "__main__":
	main() 